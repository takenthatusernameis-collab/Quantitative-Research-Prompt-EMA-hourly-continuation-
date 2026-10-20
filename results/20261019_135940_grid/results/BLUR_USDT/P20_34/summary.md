# EMA Hourly Continuation — BLUR/USDT P20_34

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.4142 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.8494 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -9.2580 |
| sortino_ratio | -4.4180 |
| max_drawdown | 0.9960 |
| cagr | -0.8865 |
| net_avg_win | 14.2528 |
| net_avg_loss | -26.3151 |
| avg_hold_time_bars | 2.8018 |
| exposure | 0.1445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
