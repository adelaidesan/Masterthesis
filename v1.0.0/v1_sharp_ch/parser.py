import json
import os.path

def parse_mm(question, parsed):
	parsed.write("\n")
	parsed.write("    "+question["question-type"].encode('utf-8')+"\n")
	parsed.write("    "+question["title"].encode('utf-8')+"\n")
	parsed.write("    choices:\n")
	choices = question["choices"]
	for choice in choices:
		parsed.write("      * "+choice.encode('utf-8')+"\n")
	parsed.write("\n")

def parse_binary(question, parsed):
	parsed.write("\n")
	parsed.write("    "+question["question-type"].encode('utf-8')+"\n")
	parsed.write("    "+question["title"].encode('utf-8')+"\n")
	parsed.write("    choices:\n")
	choices = question["choices"]
	for choice in choices:
		parsed.write("      * "+choice.encode('utf-8')+"\n")
	parsed.write("\n")

def parse_mo(question, parsed):
	parsed.write("\n")
	parsed.write("    "+question["question-type"].encode('utf-8')+"\n")
	parsed.write("    "+question["title"].encode('utf-8')+"\n")
	parsed.write("    choices:\n")
	choices = question["choices"]
	for choice in choices:
		parsed.write("      * "+choice.encode('utf-8')+"\n")
	parsed.write("\n")

def parse_integer(question, parsed):
	parsed.write("\n")
	parsed.write("    "+question["question-type"].encode('utf-8')+"\n")
	parsed.write("    "+question["title"].encode('utf-8')+"\n")
	parsed.write("\n")

def parse_text(question, parsed):
	parsed.write("\n")
	parsed.write("    "+question["question-type"].encode('utf-8')+"\n")
	parsed.write("    "+question["title"].encode('utf-8')+"\n")
	parsed.write("\n")

def parse_table(question, parsed):
	parsed.write("\n")
	parsed.write("    "+question["question-type"].encode('utf-8')+"\n")
	parsed.write("    "+question["title"].encode('utf-8')+"\n")

	columns = question["columns"]
	col_titles = "                                "
	for column in columns:
		col_titles = col_titles + column["title"].encode('utf-8') + " ("+column["type"].encode('utf-8')+")           "
	parsed.write(col_titles+"\n")

	lines = question["lines"]
	for line in lines:
		parsed.write("      * "+line.encode('utf-8')+"\n")
	parsed.write("\n")


with open("parsed.txt", "w") as parsed:
	with open("_meta_package.json") as package:
		categories = json.load(package)["order"]
		for category in categories:
			category = category.encode('utf-8')
			with open(category+"/_meta_category.json", "r") as meta_aspect:
				json_ma = json.load(meta_aspect)
				parsed.write("\n\n")
				parsed.write("#########################################")
				parsed.write("GROUP \n")
				parsed.write(" ID      "+json_ma["group_id"].encode('utf-8')+"\n")
				parsed.write(" COLOR   "+json_ma["color"].encode('utf-8')+"\n")
				parsed.write(" TITLE   "+json_ma["title"].encode('utf-8')+"\n")

				aspects = json_ma["order"]
				for aspect in aspects:
					aspect = aspect.encode('utf-8')
					with open(category+"/"+aspect+"/_meta_aspect.json", "r") as meta_question:
						json_q = json.load(meta_question)
						parsed.write("\n")
						parsed.write("  ASPECT\n")
						parsed.write("   TITLE    "+json_q["title"].encode('utf-8')+"\n")
						parsed.write("   ID       "+json_q["id"].encode('utf-8')+"\n")

						i = 1
						while os.path.isfile(category+"/"+aspect+"/"+str(i)+".json"):
							with open(category+"/"+aspect+"/"+str(i)+".json", "r") as p_question:
								try:
									q = json.load(p_question)
									type = q["question-type"].encode('utf-8')
									if (type == "multiple_multiple_solution"):
										parse_mm(q, parsed)
									elif (type == "integer_answer"):
										parse_integer(q, parsed)
									elif (type == "text_answer" or type == "text"):
										parse_text(q, parsed)
									elif (type == "binary_answer"):
										parse_binary(q, parsed)
									elif (type == "binary_answer_with_comment"):
										parse_binary(q, parsed)
									elif (type == "multiple_one_solution"):
										parse_mo(q, parsed)
									elif (type == "table"):
										parse_table(q, parsed)
									else:
										print("No parsing for type : "+type)
										print(" in file "+category+"/"+aspect+"/"+str(i)+".json\n")
								except:
									print("Error in file : "+category+"/"+aspect+"/"+str(i)+".json")
							i = i + 1