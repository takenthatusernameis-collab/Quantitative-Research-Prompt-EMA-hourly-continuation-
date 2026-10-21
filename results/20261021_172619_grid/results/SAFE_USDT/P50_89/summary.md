# EMA Hourly Continuation — SAFE/USDT P50_89

**Symbol:** SAFE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7655 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0101 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.5512 |
| sortino_ratio | -0.4189 |
| max_drawdown | 0.4219 |
| cagr | -0.1751 |
| net_avg_win | 70.2754 |
| net_avg_loss | -93.3873 |
| avg_hold_time_bars | 9.5726 |
| exposure | 0.1539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
