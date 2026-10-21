# EMA Hourly Continuation — STRK/USDT P55_100

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0422 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.0660 |
| sortino_ratio | -0.2750 |
| max_drawdown | 0.3336 |
| cagr | -0.1196 |
| net_avg_win | 76.4929 |
| net_avg_loss | -97.8333 |
| avg_hold_time_bars | 7.4441 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
