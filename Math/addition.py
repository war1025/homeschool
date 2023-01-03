
import random


def main():
   problems = set()

   while len(problems) < 24:
      total = random.randint(10, 20)
      first = random.randint(3, total - 1)

      second = total - first

      problem = "%d + %d = %d" %  (first, second, total)

      problems.add(problem)

   for problem in problems:
      print(problem)

if __name__ == "__main__":
   main()
