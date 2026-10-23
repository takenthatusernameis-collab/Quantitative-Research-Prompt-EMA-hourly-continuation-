# EMA Hourly Continuation — MOODENG/USDT P20_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 862 |
| net_profit_factor | 0.5890 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8697 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -5.9230 |
| sortino_ratio | -2.7084 |
| max_drawdown | 0.9323 |
| cagr | -0.7247 |
| net_avg_win | 34.0101 |
| net_avg_loss | -48.1554 |
| avg_hold_time_bars | 4.7923 |
| exposure | 0.2286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
