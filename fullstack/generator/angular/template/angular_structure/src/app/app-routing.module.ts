import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PageNotFoundComponent} from "./pages/page-not-found/page-not-found.component";


const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  // { path: 'login', component: LoginPageComponent },

  { path: 'not-found', component: PageNotFoundComponent, canMatch: [] },
  { path: '**', component: PageNotFoundComponent, canMatch: [] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }
