# EMA Hourly Continuation — ORCA/USDT P55_200

**Symbol:** ORCA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5418 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8371 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.5213 |
| sortino_ratio | -0.9729 |
| max_drawdown | 0.7203 |
| cagr | -0.3743 |
| net_avg_win | 46.7581 |
| net_avg_loss | -70.2443 |
| avg_hold_time_bars | 20.1308 |
| exposure | 0.3569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
