# EMA Hourly Continuation — MOODENG/USDT P55_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.5060 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.7596 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -5.4787 |
| sortino_ratio | -2.0440 |
| max_drawdown | 0.8650 |
| cagr | -0.6212 |
| net_avg_win | 35.1616 |
| net_avg_loss | -54.8935 |
| avg_hold_time_bars | 4.3958 |
| exposure | 0.1389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
