# EMA Hourly Continuation — HBAR/USDT P20_26

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0190 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.3777 |
| sortino_ratio | -0.2381 |
| max_drawdown | 0.2497 |
| cagr | -0.1027 |
| net_avg_win | 71.6472 |
| net_avg_loss | -107.2080 |
| avg_hold_time_bars | 4.8819 |
| exposure | 0.0320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
