# EMA Hourly Continuation — BOSON/USDT P55_100

**Symbol:** BOSON/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6018 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -4.0619 |
| sortino_ratio | -1.4567 |
| max_drawdown | 0.8218 |
| cagr | -0.4960 |
| net_avg_win | 41.6353 |
| net_avg_loss | -59.5905 |
| avg_hold_time_bars | 5.7624 |
| exposure | 0.1687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
