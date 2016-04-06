// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';
import { Grid } from './grid';
import { Column } from './column';

let styles = require('./library.css');
let template = require('./grid.html');


@Component({
    selector: 'library',
    directives: [Grid, CORE_DIRECTIVES],
    template: '<grid name="person grid" [rows]="people" [columns]="columns"></grid>',
    styles: [styles]
})

export class Library {
    BookInJson;

    people: Array<Person>;
    columns: Array<Column>;

    getPeople(): Array<Person> {
        return [
            { title: 'Joe', authors: 'Jackson', subtitle: 20 },
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
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                this.BookInJson = jsonResponse;
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }
}

interface Person {
    firstName: string;
    lastName: string;
    age: number;
}