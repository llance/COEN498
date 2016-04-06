// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';
import { Column } from './column';

let styles = require('./library.css');
let template = require('./library.html');


@Component({
    selector: 'library',
    inputs: ['people: people', 'columns: columns'],
    templateUrl: './src/library/library.html'
})

export class Library {
    BookInJson;

     people: Array<Person>;
     columns: Array<Column>;

     getPerson(title1: string, authors1: string, subtitle1: string): Array<Person> {
         return [
             { title: title1, authors: authors1, subtitle: subtitle1 },
         ];
     }

     getPeople(): Array<Person> {
         return [
             { title: 'Joe', authors: 'Jackson', subtitle: '20' },{ title: 'Joe', authors: 'Jackson', subtitle: '20' },
         ];
     }

     getColumns(): Array<Column> {
         return [
             new Column('title', 'Title'),
             new Column('authors', 'Authors'),
             new Column('subtitle', 'Subtitle'),
             new Column('pageCount', 'Page Count'),
             new Column('publisher', 'Publisher'),
             new Column('publishedDate', 'Published Date'),
             new Column('language', 'Language'),
         ];
     }

    constructor(public router: Router, public http: Http) {
         this.people = this.getPeople();
         this.columns = this.getColumns();
    }

    viewBooks() {
        event.preventDefault();
        contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                this.BookInJson = jsonResponse;
                alert(JSON.stringify(jsonResponse));
                this.people = this.getPerson('Janice', 'Agustin', '23');
                //for (var i = 0; i < jsonResponse.length; i++) {
                //    var item = jsonResponse[i];
                //}
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }

    getCookie(name) {
        console.log('document.cookie is ', document.cookie);
        let value = '; ' + document.cookie;
        let parts = value.split('; ' + name + '=');
        if (parts.length === 2)
            return parts.pop().split(';').shift();
    }
}

interface Person {
    title: string;
    authors: string;
    subtitle: string;
}

