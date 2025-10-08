class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line, message="Bad line detected"):
        super().__init__(f"{message}: {line.strip()}")


class FileEmpty(StudentsDataException):
    def __init__(self, filename, message="File is empty"):
        super().__init__(f"{message}: {filename}")


def read_student_data(filename):
    try:
        with open(filename, "rt") as f:
            lines = f.readlines()

            # Check if file is empty
            if not lines:
                raise FileEmpty(filename)

            students = {}

            for line in lines:
                parts = line.split()

                # Each line should contain exactly 3 elements
                if len(parts) != 3:
                    raise BadLine(line, "Incorrect number of elements")

                first_name, last_name, points_str = parts

                try:
                    points = float(points_str)
                except ValueError:
                    raise BadLine(line, "Points value is not a valid number")

                # Add or accumulate points
                key = (first_name, last_name)
                students[key] = students.get(key, 0) + points

            return students

    except FileNotFoundError:
        raise StudentsDataException(f"File '{filename}' not found.")
    except IOError as e:
        raise StudentsDataException(f"Error reading file '{filename}': {e}")


# === Program Execution (no main function) ===

filename = input("Enter Prof. Jekyll's file name: ")

try:
    data = read_student_data(filename)

    # Sort by last name, then first name
    for (first, last), points in sorted(data.items(), key=lambda x: (x[0][1], x[0][0])):
        print(f"{first} {last} \t {points}")

except StudentsDataException as e:
    print("Error:", e)
