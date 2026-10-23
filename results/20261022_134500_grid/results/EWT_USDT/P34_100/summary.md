# EMA Hourly Continuation — EWT/USDT P34_100

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5149 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -5.1312 |
| sortino_ratio | -1.8264 |
| max_drawdown | 0.8955 |
| cagr | -0.5831 |
| net_avg_win | 33.9415 |
| net_avg_loss | -51.0427 |
| avg_hold_time_bars | 8.0031 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
