# EMA Hourly Continuation — SHIB/USDT P55_89

**Symbol:** SHIB/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.4139 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.4079 |
| sortino_ratio | -2.7608 |
| max_drawdown | 0.9668 |
| cagr | -0.7407 |
| net_avg_win | 22.9737 |
| net_avg_loss | -43.3842 |
| avg_hold_time_bars | 3.7873 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
