# EMA Hourly Continuation — MOODENG/USDT P8_20

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7992 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.7316 |
| sortino_ratio | -0.5721 |
| max_drawdown | 0.4934 |
| cagr | -0.2324 |
| net_avg_win | 75.0353 |
| net_avg_loss | -98.7632 |
| avg_hold_time_bars | 7.0943 |
| exposure | 0.1708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
