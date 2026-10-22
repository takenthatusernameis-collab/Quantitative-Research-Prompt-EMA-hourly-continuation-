# EMA Hourly Continuation — EGLD/USDT P20_34

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.2951 |
| net_win_rate | 0.4031 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -11.6989 |
| sortino_ratio | -5.7045 |
| max_drawdown | 0.9994 |
| cagr | -0.9475 |
| net_avg_win | 8.8638 |
| net_avg_loss | -20.2827 |
| avg_hold_time_bars | 2.6200 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
