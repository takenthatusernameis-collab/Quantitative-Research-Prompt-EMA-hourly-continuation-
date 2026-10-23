# EMA Hourly Continuation — MINA/USDT P20_21

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1246 |
| net_profit_factor | 0.1214 |
| net_win_rate | 0.3090 |
| gross_profit_factor | 0.6494 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -17.0199 |
| sortino_ratio | -8.9592 |
| max_drawdown | 1.0000 |
| cagr | -0.9930 |
| net_avg_win | 3.5904 |
| net_avg_loss | -13.2198 |
| avg_hold_time_bars | 1.9462 |
| exposure | 0.1102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
