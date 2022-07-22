Get salary ranges from justjoin it

```
var result = "";
var salary_ranges = document.getElementsByClassName("jss258"); // change this class
for (var i = 0; i < salary_ranges.length; i++) {
    if (salary_ranges[i].textContent.includes("00")) {
        //console.log(salary_ranges[i].textContent);
        result += salary_ranges[i].textContent + "\n";
    }
}

copy(result);
```
