import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';

import {BookListComponent}   from './book-list.component';
import {MovieListComponent}     from './movie-list.component';

@Component({
  selector: 'my-app',
  template: `
    <h1>Component Router</h1>
    <nav>
      <a [routerLink]="['BookList']">Book List</a>
      <a [routerLink]="['MovieList']">Movie List</a>
    </nav>
    <router-outlet></router-outlet>
  `,
  directives: [ROUTER_DIRECTIVES]
})
@RouteConfig([
  {path: '/booklist', name: 'BookList', component: BookListComponent},
  {path: '/movielist', name: 'MovieList', component: MovieListComponent}
])
export class HomeComponent { }
