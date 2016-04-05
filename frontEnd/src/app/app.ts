import {View, Component} from 'angular2/core';
import {Location, RouteConfig, RouterLink, Router} from 'angular2/router';

import {LoggedInRouterOutlet} from './LoggedInOutlet';
import {Home} from '../home/home';
import {Login} from '../login/login';
import {Signup} from '../signup/signup';
import {Library} from '../library/library';

let template = require('./app.html');

@Component({
  selector: 'auth-app'
})
@View({
  template: template,
  directives: [ LoggedInRouterOutlet ]
})
@RouteConfig([
  { path: '/', redirectTo: ['/Login'] },
  { path: '/home', component: Home, as: 'Home' },
  { path: '/login', component: Login, as: 'Login' },
  { path: '/signup', component: Signup, as: 'Signup' },
  { path: '/library', component: Library, as: 'Library' }
])

export class App {
  constructor(public router: Router) {
  }
}
