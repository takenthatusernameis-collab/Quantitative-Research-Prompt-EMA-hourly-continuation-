# EMA Hourly Continuation — FLOW/USDT P20_26

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1244 |
| net_profit_factor | 0.2367 |
| net_win_rate | 0.3601 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -15.1257 |
| sortino_ratio | -7.7985 |
| max_drawdown | 1.0000 |
| cagr | -0.9841 |
| net_avg_win | 6.9227 |
| net_avg_loss | -16.4586 |
| avg_hold_time_bars | 1.9775 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
