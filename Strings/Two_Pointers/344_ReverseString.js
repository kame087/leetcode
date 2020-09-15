const reverseString = (s) => {
  let left = 0,
    right = s.length - 1;

  while (left < right) {
    const temp = s[right];
    s[right] = s[left];
    s[left] = temp;
    left++;
    right--;
  }

  return s;
};
