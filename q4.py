public string Foobar(int a, int b) {
    
  string result = string.Format("Sum of A: {0}", sum(range(0, a)));
  result += string.Format("; Sum of B: {0}", sum(range(0, b)));

  return result;
}
