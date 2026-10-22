# EMA Hourly Continuation — ALGO/USDT P8_55

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.5151 |
| sharpe_ratio | -4.6220 |
| sortino_ratio | -2.1130 |
| max_drawdown | 0.9325 |
| cagr | -0.6411 |
| net_avg_win | 27.2813 |
| net_avg_loss | -44.5746 |
| avg_hold_time_bars | 9.8745 |
| exposure | 0.4758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
