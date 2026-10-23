# EMA Hourly Continuation — ORCA/USDT P12_100

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -2.6505 |
| sortino_ratio | -0.8874 |
| max_drawdown | 0.6989 |
| cagr | -0.3468 |
| net_avg_win | 52.6986 |
| net_avg_loss | -75.4540 |
| avg_hold_time_bars | 23.6714 |
| exposure | 0.6090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
