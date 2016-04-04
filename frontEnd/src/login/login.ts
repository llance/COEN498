import { Component, View } from 'angular2/core';
import { Router, RouterLink } from 'angular2/router';
import { CORE_DIRECTIVES, FORM_DIRECTIVES } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { contentHeaders } from '../common/headers';

let styles   = require('./login.css');
let template = require('./login.html');

@Component({
  selector: 'login'
})
@View({
  directives: [RouterLink, CORE_DIRECTIVES, FORM_DIRECTIVES ],
  template: template,
  styles: [ styles ]
})
export class Login {
  constructor(public router: Router, public http: Http) {
  }

  login(event, username, password) {
    console.log('username is ', username, 'password is ', password);

    event.preventDefault();
    let body = JSON.stringify({username, password});
    this.http.post('http://localhost:8000/login/', body, { headers: contentHeaders })
      .subscribe(
        response => {
          console.log('routing to /home');
          this.router.parent.navigateByUrl('/home');
        },
        error => {
          alert(error.text());
          console.log(error.text());
        }
      );
  }



  signup(event) {
    event.preventDefault();
    this.router.parent.navigateByUrl('/signup');
  }
}
