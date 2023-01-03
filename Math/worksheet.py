
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


ADD_TEMPLATE = "\\opadd[carryadd=false, voperator=bottom, resultstyle=\\white]{%d}{%d} \\hfill "

SUB_TEMPLATE = "\\opsub[resultstyle=\gobble,voperator=bottom]{%d}{%d} \\hfill "


NUM_ROWS = 6
NUM_COLS = 4


def main():
   problems = set()

   while len(problems) < 24:
      total = random.randint(10, 99)
      first = random.randint(3, min(10, total - 1))

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
            SUB_TEMPLATE % (
               problems[problem_idx][2],
               problems[problem_idx][0],
            )
         )

      rows.append(
         ROW_TEMPLATE % " ".join(row_values)
      )

   print(DOC_TEMPLATE % "\n".join(rows))




if __name__ == "__main__":
   main()
