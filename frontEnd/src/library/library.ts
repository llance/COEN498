// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';

let styles = require('./library.css');
let template = require('./library.html');



@Component({
    selector: 'library',
})

@View({
    directives: [CORE_DIRECTIVES],
    template: template,
    styles: [styles]
})
export class Library {
    // var mockDataForThisTest = "json=" + encodeURI(JSON.stringify([
    //     {
    //         id: 1,
    //         firstName: "Peter",
    //         lastName: "Jhons"
    //     },
    //     {
    //         id: 2,
    //         firstName: "David",
    //         lastName: "Bowie"
    //     }
    // ]));


    // var app = angular.module('myApp', []);

    // function PeopleCtrl($scope, $http) {

    //     $scope.people = [];

    //     $scope.loadPeople = function() {
    //         var httpRequest = $http({
    //             method: 'POST',
    //             url: '/echo/json/',
    //             data: mockDataForThisTest

    //         }).success(function(data, status) {
    //             $scope.people = data;
    //         });

    //     };

    // }

    constructor(public router: Router, public http: Http) {
    }

    viewBooks() {
        event.preventDefault();
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                // this.router.parent.navigateByUrl('/home');
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }
}