# EMA Hourly Continuation — POPCAT/USDT P12_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 904 |
| net_profit_factor | 0.5650 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7816 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -6.3399 |
| sortino_ratio | -2.8797 |
| max_drawdown | 0.9502 |
| cagr | -0.7504 |
| net_avg_win | 31.4072 |
| net_avg_loss | -42.7492 |
| avg_hold_time_bars | 7.5973 |
| exposure | 0.3628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
