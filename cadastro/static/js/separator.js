function thousandSeparator(val) {
  return String(val).split("").reverse().join("").replace(/(.{3}\B)/g, "$1.").split("").reverse().join("");

}



