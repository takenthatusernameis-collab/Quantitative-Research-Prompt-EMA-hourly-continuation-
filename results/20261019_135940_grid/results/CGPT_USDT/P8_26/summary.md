# EMA Hourly Continuation — CGPT/USDT P8_26

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1517 |
| net_profit_factor | 0.4979 |
| net_win_rate | 0.4456 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -9.5671 |
| sortino_ratio | -5.2260 |
| max_drawdown | 0.9987 |
| cagr | -0.9260 |
| net_avg_win | 14.6500 |
| net_avg_loss | -23.6492 |
| avg_hold_time_bars | 3.8306 |
| exposure | 0.2641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
