# EMA Hourly Continuation — BABYDOGE/USDT P26_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 26 |
| net_profit_factor | 1.6983 |
| net_win_rate | 0.6538 |
| gross_profit_factor | 1.8670 |
| gross_win_rate | 0.6538 |
| sharpe_ratio | 0.8418 |
| sortino_ratio | 0.0656 |
| max_drawdown | 0.0316 |
| cagr | 0.0267 |
| net_avg_win | 98.2135 |
| net_avg_loss | -109.2346 |
| avg_hold_time_bars | 13.1154 |
| exposure | 0.0154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
