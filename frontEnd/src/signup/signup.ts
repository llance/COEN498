import { Component, View } from 'angular2/core';
import { Router, RouterLink } from 'angular2/router';
import { CORE_DIRECTIVES, FORM_DIRECTIVES } from 'angular2/common';
import { Http } from 'angular2/http';
import { contentHeaders } from '../common/headers';

let styles   = require('./signup.css');
let template = require('./signup.html');

@Component({
  selector: 'signup'
})
@View({
  directives: [ RouterLink, CORE_DIRECTIVES, FORM_DIRECTIVES ],
  template: template,
  styles: [ styles ]
})
export class Signup {
  constructor(public router: Router, public http: Http) {
  }

  signup(event, username, password) {
    console.log('username is ', username, 'password is ', password);
    event.preventDefault();
    let body = JSON.stringify({ username, password });
    console.log("body is : ", body);
    this.http.post('http://localhost:8000/register/', body, { headers: contentHeaders })
      .subscribe(
        response => {
          //localStorage.setItem('jwt', response.json().id_token);
          this.router.parent.navigateByUrl('/home');
        },
        error => {
          alert(error.text());
          console.log("had error from sending POST to register");
          console.log(error.text());
        }
      );
  }

  login(event) {
    event.preventDefault();
    this.router.parent.navigateByUrl('/login');
  }

}
