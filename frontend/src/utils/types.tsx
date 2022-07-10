export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
}

export interface Course {
  id: number;
  name: string;
}

export interface Mentor {
  id: number;
  user: User;
  course: Course;
}

export interface Section {
  id: number;
  mentor: Mentor;
  capacity: number;
  description: string;
}

export interface Student {
  id: number;
  user: User;
  section: Section;
  course: Course;
  active: boolean;
  banned: boolean;
}
