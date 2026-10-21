# EMA Hourly Continuation — XPR/USDT P26_89

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7507 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.7833 |
| sortino_ratio | -0.4787 |
| max_drawdown | 0.4456 |
| cagr | -0.1977 |
| net_avg_win | 73.9567 |
| net_avg_loss | -94.6895 |
| avg_hold_time_bars | 15.9518 |
| exposure | 0.2560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
