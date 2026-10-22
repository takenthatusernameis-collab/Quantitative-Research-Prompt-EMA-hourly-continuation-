# EMA Hourly Continuation — JASMY/USDT P8_21

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1690 |
| net_profit_factor | 0.3807 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.7300 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -11.7383 |
| sortino_ratio | -6.7807 |
| max_drawdown | 0.9998 |
| cagr | -0.9680 |
| net_avg_win | 8.3971 |
| net_avg_loss | -16.8527 |
| avg_hold_time_bars | 2.7527 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
