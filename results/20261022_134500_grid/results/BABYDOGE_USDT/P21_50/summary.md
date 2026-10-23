# EMA Hourly Continuation — BABYDOGE/USDT P21_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 32 |
| net_profit_factor | 1.3326 |
| net_win_rate | 0.5938 |
| gross_profit_factor | 1.4482 |
| gross_win_rate | 0.5938 |
| sharpe_ratio | 0.5212 |
| sortino_ratio | 0.0436 |
| max_drawdown | 0.0307 |
| cagr | 0.0180 |
| net_avg_win | 97.1553 |
| net_avg_loss | -106.5581 |
| avg_hold_time_bars | 23.0938 |
| exposure | 0.0334 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
