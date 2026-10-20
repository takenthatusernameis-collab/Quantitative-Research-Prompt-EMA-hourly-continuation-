# EMA Hourly Continuation — SUSHI/USDT P12_20

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1505 |
| net_profit_factor | 0.2746 |
| net_win_rate | 0.3827 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4213 |
| sharpe_ratio | -14.0595 |
| sortino_ratio | -7.8187 |
| max_drawdown | 1.0000 |
| cagr | -0.9814 |
| net_avg_win | 6.5706 |
| net_avg_loss | -14.8377 |
| avg_hold_time_bars | 2.1807 |
| exposure | 0.1485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
