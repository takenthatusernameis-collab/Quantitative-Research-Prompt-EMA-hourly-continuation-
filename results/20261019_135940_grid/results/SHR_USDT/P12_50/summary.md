# EMA Hourly Continuation — SHR/USDT P12_50

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1366 |
| net_profit_factor | 0.4637 |
| net_win_rate | 0.3499 |
| gross_profit_factor | 0.7022 |
| gross_win_rate | 0.3529 |
| sharpe_ratio | -10.9288 |
| sortino_ratio | -5.6307 |
| max_drawdown | 0.9990 |
| cagr | -0.9350 |
| net_avg_win | 18.0723 |
| net_avg_loss | -20.9780 |
| avg_hold_time_bars | 5.4854 |
| exposure | 0.3391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
