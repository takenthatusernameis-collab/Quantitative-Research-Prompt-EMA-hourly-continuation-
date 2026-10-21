# EMA Hourly Continuation — PHA/USDT P55_144

**Symbol:** PHA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -2.3122 |
| sortino_ratio | -0.6140 |
| max_drawdown | 0.5366 |
| cagr | -0.2467 |
| net_avg_win | 65.8568 |
| net_avg_loss | -80.2928 |
| avg_hold_time_bars | 13.7436 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
