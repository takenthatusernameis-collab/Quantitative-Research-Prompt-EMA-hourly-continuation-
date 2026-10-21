# EMA Hourly Continuation — BABYDOGE/USDT P21_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 34 |
| net_profit_factor | 1.1563 |
| net_win_rate | 0.5588 |
| gross_profit_factor | 1.2563 |
| gross_win_rate | 0.5588 |
| sharpe_ratio | 0.2804 |
| sortino_ratio | 0.0238 |
| max_drawdown | 0.0348 |
| cagr | 0.0097 |
| net_avg_win | 95.5639 |
| net_avg_loss | -104.6822 |
| avg_hold_time_bars | 24.2353 |
| exposure | 0.0373 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
