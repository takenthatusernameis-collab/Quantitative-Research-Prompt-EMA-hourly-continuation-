# EMA Hourly Continuation — AURORA/USDT P100_144

**Symbol:** AURORA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.4701 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -4.9031 |
| sortino_ratio | -1.3604 |
| max_drawdown | 0.8151 |
| cagr | -0.4874 |
| net_avg_win | 42.1956 |
| net_avg_loss | -72.3989 |
| avg_hold_time_bars | 4.8225 |
| exposure | 0.0840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
