# EMA Hourly Continuation — HBAR/USDT P26_89

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.5616 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -5.2595 |
| sortino_ratio | -1.9894 |
| max_drawdown | 0.9159 |
| cagr | -0.6209 |
| net_avg_win | 34.5834 |
| net_avg_loss | -54.2035 |
| avg_hold_time_bars | 8.3144 |
| exposure | 0.2729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
