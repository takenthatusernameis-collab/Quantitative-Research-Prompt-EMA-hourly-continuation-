# EMA Hourly Continuation — MOODENG/USDT P20_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7944 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.7279 |
| sortino_ratio | -0.5589 |
| max_drawdown | 0.4836 |
| cagr | -0.2283 |
| net_avg_win | 77.6953 |
| net_avg_loss | -93.2730 |
| avg_hold_time_bars | 15.6161 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
