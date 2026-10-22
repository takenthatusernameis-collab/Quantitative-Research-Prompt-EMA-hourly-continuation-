# EMA Hourly Continuation — AUCTION/USDT P50_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.4583 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7879 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -4.1504 |
| sortino_ratio | -0.9430 |
| max_drawdown | 0.6982 |
| cagr | -0.3651 |
| net_avg_win | 52.9474 |
| net_avg_loss | -86.2446 |
| avg_hold_time_bars | 5.1294 |
| exposure | 0.0592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
