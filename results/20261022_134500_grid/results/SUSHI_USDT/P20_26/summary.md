# EMA Hourly Continuation — SUSHI/USDT P20_26

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1262 |
| net_profit_factor | 0.2716 |
| net_win_rate | 0.3677 |
| gross_profit_factor | 0.8569 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -14.2907 |
| sortino_ratio | -7.3291 |
| max_drawdown | 0.9999 |
| cagr | -0.9794 |
| net_avg_win | 8.0356 |
| net_avg_loss | -17.2030 |
| avg_hold_time_bars | 1.8827 |
| exposure | 0.1075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
