import React, { useEffect, useState } from "react";
import { Student as StudentType } from "../utils/types";
import { useParams } from "react-router";

interface StudentProps {}

export const Student = ({}: StudentProps) => {
  const [student, setStudent] = useState<StudentType>(undefined as never);
  const { id } = useParams<string>();

  useEffect(() => {
    fetch(`/api/students/${id}/details`)
      .then((res) => res.json())
      .then((data) => {
        setStudent(data);
      });
  }, []);

  return (
    <div>
      <h1>Student</h1>
      {student && (
        <div>
          <p>
            {student.user.first_name} {student.user.last_name} (id: {id})
          </p>
          <p>
            Course: {student.course.name} (id: {student.course.id})
          </p>
          <p>
            Mentor: {student.section.mentor.user.first_name}{" "}
            {student.section.mentor.user.last_name}
          </p>
        </div>
      )}
    </div>
  );
};
