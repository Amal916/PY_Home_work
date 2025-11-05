frontend = {"Alice", "Bob", "Charlie"}
backend = {"David", "Bob", "Eve"}

backend.add("Frank")
frontend.remove("Alice")

both_courses = frontend & backend
print("Students in both courses:", both_courses)

only_backend = backend - frontend
print("Only in Backend:", only_backend)

total_unique = len(frontend | backend)
print("Total unique students:", total_unique)

courses = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")

expanded_courses = {**courses, "Fullstack": courses["Frontend"] + courses["Backend"]}
print("Courses with Fullstack added:", expanded_courses)
