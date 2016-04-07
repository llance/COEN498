import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';


let styles = require('./home.css');
let template = require('./home.html');


@Component({
  selector: 'home',
})

@View({
  directives: [CORE_DIRECTIVES],
  template: template,
  styles: [styles]
})
export class Home {
    ibsnForm: ControlGroup;
    upcForm: ControlGroup;

    constructor(public router: Router, public http: Http, fb: FormBuilder) {
        this.ibsnForm = fb.group({
          ibsnNumber: ['', Validators.required]
      });
        this.upcForm = fb.group({
            upcNumber: ['', Validators.required]
        });
  }

  submitIBSN(event) {
      var ibsnNum = this.ibsnForm.value.ibsnNumber;
      console.log('submitIBSN called! IBSN number is ', ibsnNum);
      event.preventDefault();
      let body = JSON.stringify({ ibsnNum });

      console.log('contentHeaders is', contentHeaders);

      
      this.http.post('http://localhost:8000/books/', body, { headers: contentHeaders })
        .subscribe(
          response => {
            var jsonResponse = response.json();
            console.log('response received!', jsonResponse.title);
                        // this.router.parent.navigateByUrl('/home');
          },
          error => {
            alert(error.text());
            console.log(error.text());
          }
        );
  }

  submitUPC(event) {
      var upcNum = this.upcForm.value.upcNumber;
      console.log('submitIBSN called! UPC number is ', upcNum);
      event.preventDefault();
      let body = JSON.stringify({ upcNum });
      this.http.post('http://localhost:8000/movies/', body, { headers: contentHeaders })
          .subscribe(
          response => {
              var jsonResponse = response.json();
              console.log('response received!', jsonResponse.title);
              // this.router.parent.navigateByUrl('/home');
          },
          error => {
              alert(error.text());
              console.log(error.text());
          }
          );
  }

  viewLibrary() {
      this.router.parent.navigateByUrl('/library');
  }

  logout() {
    localStorage.removeItem('jwttoken');
    localStorage.removeItem('restsessiontoken');
    this.router.parent.navigateByUrl('/login');
  }

}
