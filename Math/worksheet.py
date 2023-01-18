
import random


DOC_TEMPLATE = """

\\documentclass[20pt,letterpaper]{extarticle}
\\usepackage{xlop}

\\setlength{\\voffset}{-0.75in}
\\setlength{\\textheight}{9.0in}

\\newcommand\gobble[1]{}

\\begin{document}

%s

\\end{document}

"""

ROW_TEMPLATE = """

\\hspace*{\\fill}

%s


"""


ADD_TEMPLATE = "\\opadd[carryadd=false, voperator=bottom, resultstyle=\gobble]{{{first}}}{{{second}}} \\hfill "

SUB_TEMPLATE = "\\opsub[resultstyle=\gobble,voperator=bottom]{{{total}}}{{{first}}} \\hfill "


NUM_ROWS = 6
NUM_COLS = 4


def main():
   add_rows = generateRows(ADD_TEMPLATE)

   sub_rows = generateRows(SUB_TEMPLATE)


   add_str = "\n".join(add_rows)
   sub_str = "\n".join(sub_rows)

   print(DOC_TEMPLATE % "\n".join([add_str, "\\clearpage", sub_str]))

def generateRows(templateStr):
   problems = set()

   while len(problems) < 24:
      total = random.randint(10, 99)
      first = random.randint(3, total - 1)

      second = total - first

      #problem = "%d + %d = %d" %  (first, second, total)

      problem = (first, second, total)

      problems.add(problem)

   problems = list(problems)

   rows = []

   for row_idx in range(NUM_ROWS):

      row_values = []

      for col_idx in range(NUM_COLS):
         problem_idx = row_idx * NUM_COLS + col_idx

         row_values.append(
            templateStr.format(
               first = problems[problem_idx][0],
               second = problems[problem_idx][1],
               total = problems[problem_idx][2],
            )
         )

      rows.append(
         ROW_TEMPLATE % " ".join(row_values)
      )

   return rows




if __name__ == "__main__":
   main()
