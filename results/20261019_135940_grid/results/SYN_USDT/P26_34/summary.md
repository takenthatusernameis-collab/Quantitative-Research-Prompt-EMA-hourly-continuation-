# EMA Hourly Continuation — SYN/USDT P26_34

**Symbol:** SYN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.3499 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.7770 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -10.2405 |
| sortino_ratio | -4.7277 |
| max_drawdown | 0.9977 |
| cagr | -0.9113 |
| net_avg_win | 12.3469 |
| net_avg_loss | -24.2850 |
| avg_hold_time_bars | 2.4677 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
