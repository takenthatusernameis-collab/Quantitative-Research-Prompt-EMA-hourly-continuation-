# EMA Hourly Continuation — MOODENG/USDT P8_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.8157 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -1.4892 |
| sortino_ratio | -0.4736 |
| max_drawdown | 0.3994 |
| cagr | -0.1981 |
| net_avg_win | 80.9607 |
| net_avg_loss | -95.4327 |
| avg_hold_time_bars | 28.3382 |
| exposure | 0.6397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
