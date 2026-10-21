# EMA Hourly Continuation — FET/USDT P8_55

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.8587 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0273 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.2248 |
| sortino_ratio | -0.4482 |
| max_drawdown | 0.4663 |
| cagr | -0.1897 |
| net_avg_win | 75.5291 |
| net_avg_loss | -90.4284 |
| avg_hold_time_bars | 15.0906 |
| exposure | 0.4465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
