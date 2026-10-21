# EMA Hourly Continuation — MASK/USDT P21_50

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6422 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -3.4998 |
| sortino_ratio | -1.2097 |
| max_drawdown | 0.7612 |
| cagr | -0.4284 |
| net_avg_win | 48.0184 |
| net_avg_loss | -69.5927 |
| avg_hold_time_bars | 7.2650 |
| exposure | 0.1932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
