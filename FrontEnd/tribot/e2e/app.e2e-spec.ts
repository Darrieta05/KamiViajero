import { KamiviajeroPage } from './app.po';

describe('kamiviajero App', () => {
  let page: KamiviajeroPage;

  beforeEach(() => {
    page = new KamiviajeroPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
