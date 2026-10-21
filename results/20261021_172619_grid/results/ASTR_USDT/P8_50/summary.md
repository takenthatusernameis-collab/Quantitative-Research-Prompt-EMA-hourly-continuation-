# EMA Hourly Continuation — ASTR/USDT P8_50

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.7428 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -3.0029 |
| sortino_ratio | -1.1596 |
| max_drawdown | 0.7520 |
| cagr | -0.4147 |
| net_avg_win | 59.2825 |
| net_avg_loss | -77.2435 |
| avg_hold_time_bars | 14.1049 |
| exposure | 0.4685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
