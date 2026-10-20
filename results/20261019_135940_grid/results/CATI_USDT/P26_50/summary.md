# EMA Hourly Continuation — CATI/USDT P26_50

**Symbol:** CATI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.4142 |
| net_win_rate | 0.3879 |
| gross_profit_factor | 0.7250 |
| gross_win_rate | 0.4181 |
| sharpe_ratio | -10.2108 |
| sortino_ratio | -4.6760 |
| max_drawdown | 0.9926 |
| cagr | -0.9024 |
| net_avg_win | 21.0069 |
| net_avg_loss | -32.1397 |
| avg_hold_time_bars | 4.0302 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
