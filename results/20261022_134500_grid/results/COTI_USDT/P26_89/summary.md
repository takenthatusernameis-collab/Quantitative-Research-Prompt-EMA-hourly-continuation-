# EMA Hourly Continuation — COTI/USDT P26_89

**Symbol:** COTI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.5843 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.8993 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -4.5573 |
| sortino_ratio | -1.7890 |
| max_drawdown | 0.8952 |
| cagr | -0.5840 |
| net_avg_win | 33.4312 |
| net_avg_loss | -51.0690 |
| avg_hold_time_bars | 8.0479 |
| exposure | 0.2901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
