# EMA Hourly Continuation — CELR/USDT P26_144

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6688 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -2.5332 |
| sortino_ratio | -0.7166 |
| max_drawdown | 0.5877 |
| cagr | -0.2816 |
| net_avg_win | 63.4877 |
| net_avg_loss | -77.6647 |
| avg_hold_time_bars | 27.5400 |
| exposure | 0.4985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
