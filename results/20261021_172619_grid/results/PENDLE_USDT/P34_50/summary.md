# EMA Hourly Continuation — PENDLE/USDT P34_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.8371 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1127 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -0.8818 |
| sortino_ratio | -0.2081 |
| max_drawdown | 0.2512 |
| cagr | -0.0920 |
| net_avg_win | 78.3853 |
| net_avg_loss | -104.7910 |
| avg_hold_time_bars | 5.7491 |
| exposure | 0.0698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
