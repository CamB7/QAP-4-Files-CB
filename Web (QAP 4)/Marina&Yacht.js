// Decscription: St.John's Marina and Yacht Club - Yearly Member Receipt
// Author: Cameron Boyer
// Date: March 20, 2025

// Define constants
const cur2Format = new Intl.NumberFormat('en-CA', {
  style: 'currency',
  currency: 'CAD',
  minimumFractionDigits: '2',
  maximumFractionDigits: '2',
});

const per0Format = new Intl.NumberFormat('en-CA', {
  style: 'percent',
  minimumFractionDigits: '0',
  maximumFractionDigits: '0',
});

const num0Format = new Intl.NumberFormat('en-CA', {
  style: 'decimal',
  minimumFractionDigits: '0',
  maximumFractionDigits: '0',
});

const SITE_EVEN = 80.0;
const SITE_ODD = 120.0;
const ALT_MEMBER = 5.0;

const CLEAN_SERV = 50.0;
const VID_SERV = 35.0;

const EXEC_DUES = 150.0;
const REG_DUES = 75.0;

const PROCESS_FEE = 59.99;
const CANCEL_FEE_RATE = 0.6;

const HST_RATE = 0.15;

function toTitleCase(str) {
  // Capitalizes the first letter of each word in a string
  return str.replace(
    /\w\S*/g, // A regular expression (regex) - matches characters that are not white space.
    (text) => text.charAt(0).toUpperCase() + text.substring(1).toLowerCase() // The arrow operator is used to define a function.
    //^^^ - Function perameter
  );
}

// Gather user input
let curDate = prompt('Enter the current date (YYYY/MM/DD): ', '2025/03/20');
let year = parseInt(curDate.substring(0, 4)); // or year = curDate.getFullYear(); , getMonth() and getDate()
let month = parseInt(curDate.substring(5, 7));
let day = parseInt(curDate.substring(8, 10));
curDate = new Date(year, month - 1, day);

let siteNum = parseInt(prompt('Enter the site number(1-100): ', '001'));

let memberName = prompt("Enter the member's name: ", 'John Doe');
if (memberName) {
  // If the user enters a name (checks for null or cancel), capitalize the first letter of each word.
  memberName = toTitleCase(memberName);
}
let stAddress = prompt("Enter the member's street address: ", '123 Main St.');
if (stAddress) {
  stAddress = toTitleCase(stAddress);
}
let city = prompt("Enter the member's city: ", "St. John's");
if (city) {
  city = toTitleCase(city);
}

let province = prompt("Enter the member's province : ", 'NL').toUpperCase();
let postalCode = prompt(
  "Enter the member's postal code: ",
  'A0A0A0'
).toUpperCase();
let phoneNum = prompt("Enter the member's phone number: ", '(123)456-7890');
let cellNum = prompt("Enter the member's cell number: ", '(123)456-7890');

let memType = prompt(
  'Enter the member type (E for Executive, S for Standard): ',
  'S'
).toUpperCase();
if (memType === 'E') {
  memType = 'Executive';
} else {
  memType = 'Standard';
}

let altMemberNum = parseInt(
  prompt('Enter the number of alternate members (0-5): ', '0')
);

let cleanServ = prompt(
  'Would you like to add cleaning service (Y/N): ',
  'Y'
).toUpperCase();
if (cleanServ === 'Y') {
  cleanServ = 'Yes';
} else {
  cleanServ = 'No';
}

let vidServ = prompt(
  'Would you like to add video service (Y/N): ',
  'Y'
).toUpperCase();
if (vidServ === 'Y') {
  vidServ = 'Yes';
} else {
  vidServ = 'No';
}

// Calculate the site charges
let siteCharges = 0.0;
if (siteNum % 2 === 0) {
  siteCharges = SITE_EVEN;
}
if (siteNum % 2 === 1) {
  siteCharges = SITE_ODD;
}
if (altMemberNum > 0) {
  siteCharges += ALT_MEMBER * altMemberNum;
}

// Calculate the service charges
let extraCharges = 0.0;
if (cleanServ === 'Yes') {
  extraCharges += CLEAN_SERV;
}
if (vidServ === 'Yes') {
  extraCharges += VID_SERV;
}

// Calculate subtotal
let subTotal = siteCharges + extraCharges;
let hst = subTotal * HST_RATE;
let totalMonthly = subTotal + hst;

// Calculate the monthly dues
let monthlyDues = 0.0;
if (memType === 'Executive') {
  monthlyDues = EXEC_DUES;
}
if (memType === 'Standard') {
  monthlyDues = REG_DUES;
}

// Calculate the total monthly fee, total yearly fee and monthly payment
let totalMonthlyFee = totalMonthly + monthlyDues;
let totalYearlyFee = totalMonthlyFee * 12;
let monthlyPayment = (totalYearlyFee + PROCESS_FEE) / 12;

// Calculate cancellation fee
let cancelFee = siteCharges * 12 * CANCEL_FEE_RATE;

// Output the receipt to the user on the webpage

if (memType === 'Executive') {
  monthlyDues = EXEC_DUES;
} else {
  monthlyDues = REG_DUES;
}

// Calculate the total monthly fee, total yearly fee and monthly payment
totalMonthlyFee = totalMonthly + monthlyDues;
totalYearlyFee = totalMonthlyFee * 12;
monthlyPayment = (totalYearlyFee + PROCESS_FEE) / 12;

// Calculate cancellation fee
cancelFee = siteCharges * 12 * CANCEL_FEE_RATE;

// Output the receipt to the user on the webpage
let bigSpace =
  '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';

document.write('<table class = "receipttable">');
document.write('<tr colspan="2">');
document.write('<th colspan="2">St. John\'s Marina & Yacht Club<br />');
document.write('Yearly Member Receipt</th>');
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write('<td><br />Customer Name and Address:<br /><br />');
document.write(memberName + '<br />');
document.write(stAddress + '<br />');
document.write(city + ', ' + province + ', ' + postalCode + '<br /><br />');
document.write('Phone: ' + phoneNum + ' (H)<br />');
document.write(
  '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + cellNum + ' (C)<br /></td>'
);
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Site #: ' +
    siteNum +
    bigSpace +
    '&nbsp;&nbsp;' +
    'Member Type: ' +
    memType +
    '</td>'
);
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Alternate Members: &nbsp;&nbsp;' +
    bigSpace +
    bigSpace +
    altMemberNum +
    '<br />'
);
document.write(
  'Weekly site cleaning: &nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    cleanServ +
    '<br />'
);
document.write(
  'Video surveillance:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    '' +
    vidServ +
    '<br />'
);
document.write('</td>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Site Charges: &nbsp;' +
    bigSpace +
    bigSpace +
    cur2Format.format(siteCharges) +
    '<br />'
);
document.write(
  'Extra Charges: &nbsp;' +
    bigSpace +
    bigSpace +
    cur2Format.format(extraCharges) +
    '</td>'
);
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Subtotal: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    bigSpace +
    cur2Format.format(subTotal) +
    '<br />'
);
document.write(
  'Sales Tax (HST): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    cur2Format.format(hst) +
    '</td>'
);
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Total Monthly Charges: &nbsp;&nbsp;&nbsp;' +
    bigSpace +
    cur2Format.format(totalMonthlyFee) +
    '<br />'
);
document.write(
  'Monthly Dues: &nbsp;' +
    bigSpace +
    bigSpace +
    cur2Format.format(monthlyDues) +
    '</td>'
);
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Total monthly fees: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    cur2Format.format(totalMonthlyFee) +
    '<br />'
);
document.write(
  'Total yearly fees: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    cur2Format.format(totalYearlyFee) +
    '</td>'
);
document.write('</tr>');

document.write('<tr rowspan="2">');
document.write(
  '<td>Monthly Payment: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    cur2Format.format(monthlyPayment) +
    '</td>'
);

document.write('<tr rowspan="2">');
document.write(
  '<td>Issued: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    curDate.toISOString().split('T')[0] +
    '<br />' +
    '<br />'
);
document.write(
  'HST Reg No: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    '549-33-5849-47' +
    '<br />' +
    '<br />'
);
document.write(
  'Cancellation Fee: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
    bigSpace +
    '&nbsp;' +
    cur2Format.format(cancelFee) +
    '</td>'
);
document.write('</tr>');

document.write('</table>');
