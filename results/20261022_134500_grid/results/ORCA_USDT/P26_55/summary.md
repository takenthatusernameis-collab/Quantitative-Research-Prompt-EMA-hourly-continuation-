# EMA Hourly Continuation — ORCA/USDT P26_55

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.5759 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -5.4453 |
| sortino_ratio | -2.1907 |
| max_drawdown | 0.9363 |
| cagr | -0.6589 |
| net_avg_win | 32.4018 |
| net_avg_loss | -51.5176 |
| avg_hold_time_bars | 5.6345 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
