# EMA Hourly Continuation — VET/USDT P26_200

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.7224 |
| sortino_ratio | -0.7667 |
| max_drawdown | 0.6255 |
| cagr | -0.3087 |
| net_avg_win | 55.5373 |
| net_avg_loss | -81.9216 |
| avg_hold_time_bars | 30.8941 |
| exposure | 0.5701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
