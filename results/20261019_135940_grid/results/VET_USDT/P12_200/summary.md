# EMA Hourly Continuation — VET/USDT P12_200

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.6363 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9214 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.6887 |
| sortino_ratio | -0.7481 |
| max_drawdown | 0.6348 |
| cagr | -0.2960 |
| net_avg_win | 55.0998 |
| net_avg_loss | -79.7347 |
| avg_hold_time_bars | 43.2216 |
| exposure | 0.7623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
