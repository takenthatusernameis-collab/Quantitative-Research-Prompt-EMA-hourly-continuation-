# EMA Hourly Continuation — BABYDOGE/USDT P34_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 41 |
| net_profit_factor | 1.1613 |
| net_win_rate | 0.5610 |
| gross_profit_factor | 1.2662 |
| gross_win_rate | 0.5610 |
| sharpe_ratio | 0.3191 |
| sortino_ratio | 0.0298 |
| max_drawdown | 0.0436 |
| cagr | 0.0121 |
| net_avg_win | 96.5751 |
| net_avg_loss | -106.2620 |
| avg_hold_time_bars | 20.0000 |
| exposure | 0.0371 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
