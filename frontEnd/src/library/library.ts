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
    inputs: ['item: item', 'columns: columns'],
    templateUrl: './src/library/library.html'
})

export class Library {
    BookInJson;

     item: Array<any>;
     columns: Array<Column>;

//     getPerson(title1: string, authors1: string, subtitle1: string): Array<Book> {
//         return [
//             { title: title1, authors: authors1, subtitle: subtitle1 },
//         ];
//     }

     getBooks(): Array<Book> {
         return [
             { title: 'Joe', authors: 'Jackson', subtitle: '20', pageCount: '10', publisher: 'someone', publishedDate: 'blah', language: 'english' },{ title: 'Joe', authors: 'Jackson', subtitle: '20', pageCount: '10', publisher: 'authors', publishedDate: 'blah', language: 'english' },
         ];
     }

     getColumnsBooks(): Array<Column> {
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

     getMovies(): Array<Movie> {
         return [
             { title: 'Joe', directors: 'Jackson', subtitle: '20', length: '10', publisher: 'someone', publishedDate: 'blah', language: 'english' },{ title: 'Joe', directors: 'Jackson', subtitle: '20', length: '10', publisher: 'someone', publishedDate: 'blah', language: 'english' },
         ];
     }

    getColumnsMovies(): Array<Column> {
         return [
             new Column('title', 'Title'),
             new Column('directors', 'Directors'),
             new Column('subtitle', 'Subtitle'),
             new Column('length', 'Length'),
             new Column('publisher', 'Publisher'),
             new Column('publishedDate', 'Published Date'),
             new Column('language', 'Language'),
         ];
     }

     getMusic(): Array<Music> {
         return [
             { title: 'Joe', artist: 'Jackson', album: '20', length: '10', publisher: 'someone', publishedDate: 'blah', language: 'english' },{ title: 'Joe', artist: 'Jackson', album: '20', length: '10', publisher: 'someone', publishedDate: 'blah', language: 'english' },
         ];
     }

    getColumnsMusic(): Array<Column> {
         return [
             new Column('title', 'Title'),
             new Column('artist', 'Artist'),
             new Column('album', 'Album'),
             new Column('length', 'Length'),
             new Column('publisher', 'Publisher'),
             new Column('publishedDate', 'Published Date'),
             new Column('language', 'Language'),
         ];
     }

    constructor(public router: Router, public http: Http) {
         this.item = this.getBooks();
         this.columns = this.getColumnsBooks();
    }

    viewBooks() {
        event.preventDefault();
        contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse))
                this.columns = this.getColumnsBooks();
                this.BookInJson = jsonResponse;
                alert(JSON.stringify(jsonResponse));
                //this.getPerson('Janice', 'Agustin', '23');
                for (var i = 0; i < jsonResponse.length; i++) {
                    var item = jsonResponse[i];
                    console.log('string item', JSON.stringify(item));
                    //this.people = JSON.stringify(item);
                }
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }

    viewMovies() {
        event.preventDefault();
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse))
                this.columns = this.getColumnsMovies();
                this.item = this.getMovies();
                this.BookInJson = jsonResponse;
                alert(JSON.stringify(jsonResponse));
                //this.getPerson('Janice', 'Agustin', '23');
                for (var i = 0; i < jsonResponse.length; i++) {
                    var item = jsonResponse[i];
                    console.log('string item', JSON.stringify(item));
                    this.item = JSON.stringify(item);
                }
            },
            error => {
                alert(error.text());
                console.log(error.text());
            });
    }

    viewMusic() {
        event.preventDefault();
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse))
                this.columns = this.getColumnsMusic();
                this.item = this.getMusic();
                this.BookInJson = jsonResponse;
                alert(JSON.stringify(jsonResponse));
                //this.getPerson('Janice', 'Agustin', '23');
                for (var i = 0; i < jsonResponse.length; i++) {
                    var item = jsonResponse[i];
                    console.log('string item', JSON.stringify(item));
                    this.item = JSON.stringify(item);
                }
            },
            error => {
                alert(error.text());
                console.log(error.text());
            });
    }

    getCookie(name) {
        console.log('document.cookie is ', document.cookie);
        let value = '; ' + document.cookie;
        let parts = value.split('; ' + name + '=');
        if (parts.length === 2)
            return parts.pop().split(';').shift();
    }
}

interface Book {
    title: string;
    authors: string;
    subtitle: string;
    pageCount: string;
    publisher: string;
    publishedDate: string;
    language: string;
}

interface Movie {
    title: string;
    directors: string;
    subtitle: string;
    length: string;
    publisher: string;
    publishedDate: string;
    language: string;
}

interface Music {
    title: string;
    artist: string;
    album: string;
    length: string;
    publisher: string;
    publishedDate: string;
    language: string;
}

