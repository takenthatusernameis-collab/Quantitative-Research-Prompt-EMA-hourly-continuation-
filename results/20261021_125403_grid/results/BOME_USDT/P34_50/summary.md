# EMA Hourly Continuation — BOME/USDT P34_50

**Symbol:** BOME/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.8379 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.0992 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -0.8162 |
| sortino_ratio | -0.1926 |
| max_drawdown | 0.2235 |
| cagr | -0.0858 |
| net_avg_win | 73.9187 |
| net_avg_loss | -98.7217 |
| avg_hold_time_bars | 4.4981 |
| exposure | 0.0546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
