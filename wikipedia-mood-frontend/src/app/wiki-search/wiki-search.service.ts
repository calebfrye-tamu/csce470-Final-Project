import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WikiSearchService {

  private apiUrl = 'http://localhost:12000/search';  // Backend URL

  constructor(private http: HttpClient) {}

  searchArticles(query: string, mood: string): Observable<any> {
    const requestBody = { query, mood };
    console.log(`Searching for articles relating to '${query}' with mood '${mood}'`);
    return this.http.post<any>(this.apiUrl, requestBody);
  }
}
