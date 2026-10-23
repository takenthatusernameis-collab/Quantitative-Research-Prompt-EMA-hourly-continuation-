# EMA Hourly Continuation — MOCA/USDT P26_89

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5931 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -4.9142 |
| sortino_ratio | -1.8112 |
| max_drawdown | 0.8840 |
| cagr | -0.5895 |
| net_avg_win | 43.0522 |
| net_avg_loss | -63.1390 |
| avg_hold_time_bars | 9.6661 |
| exposure | 0.3062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
