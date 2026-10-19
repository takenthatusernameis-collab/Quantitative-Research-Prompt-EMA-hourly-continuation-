# EMA Hourly Continuation — ALGO/USDT P50_89

**Symbol:** ALGO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5043 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -4.9720 |
| sortino_ratio | -1.7694 |
| max_drawdown | 0.8896 |
| cagr | -0.5773 |
| net_avg_win | 29.2347 |
| net_avg_loss | -54.2665 |
| avg_hold_time_bars | 4.3265 |
| exposure | 0.1253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
