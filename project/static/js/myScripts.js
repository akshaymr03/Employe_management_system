function validateForm() {
    var na = document.forms["myForm"]["name"].value;
    if (na == "") {
      alert("Name must be filled out");
      
    }
    var d = document.forms["myForm"]["dob"].value;
    if (d == "") {
      alert("Date must be filled out");
      
    }
    var mail = document.forms["myForm"]["email"].value;
    if (mail == "") {
      alert("Email must be filled out");
      
    }
    var g = document.forms["myForm"]["gender"].value;
    if (g == "") {
      alert("Gender must be filled out");
      
    }
    var ad = document.forms["myForm"]["addres"].value;
    if (ad == "") {
      alert("Address must be filled out");
      
    }
    var nu = document.forms["myForm"]["numbers"].value;
    if (nu == "") {
      alert("Number must be filled out");
      
    }
    var pic = document.forms["myForm"]["photo"].value;
    if (pic == "") {
      alert("Photo must be uploaded");
      
    }
    var de = document.forms["myForm"]["degree"].value;
    if (de == "") {
      alert("Qualification must be filled out");
      
    }
    var inst = document.forms["myForm"]["institution"].value;
    if (inst == "") {
      alert("Institution Name must be filled out");
      
    }
    var acnum = document.forms["myForm"]["acnumber"].value;
    if (acnum == "") {
      alert("Account Number name must be filled out");
      
    }
    var b = document.forms["myForm"]["branch"].value;
    if (b == "") {
      alert("Branch name must be filled out");
      
    }
    var ifs = document.forms["myForm"]["ifsc"].value;
    if (ifs == "") {
      alert("IFSC Code must be filled out");
      
    }
    var eid = document.forms["myForm"]["emp_id"].value;
    if (eid == "") {
      alert("Employee ID  must be filled out");
      
    }
    var dept = document.forms["myForm"]["depaetment"].value;
    if (dept == "") {
      alert("Department Name must be filled out");
      
    }
    var doj = document.forms["myForm"]["date_of_join"].value;
    if (doj == "") {
      alert("Date Of Join must be filled out");
      
    }
    var po = document.forms["myForm"]["position"].value;
    if (po == "") {
      alert("Position must be filled out");
      
    }
    var sa = document.forms["myForm"]["salary"].value;
    if (sa == "") {
      alert("Salary must be filled out");
      
    }
    var st = document.forms["myForm"]["status"].value;
    if (st == "") {
      alert("Status must be filled out");
      
    }
    var c = document.forms["myForm"]["cv"].value;
    if (c == "") {
      alert("CV must be uploaded");
      
    }
    var bo = document.forms["myForm"]["bound"].value;
    if (bo == "") {
      alert("Bound must be uploaded");
      
    }
}