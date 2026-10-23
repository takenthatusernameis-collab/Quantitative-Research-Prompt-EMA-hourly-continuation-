# EMA Hourly Continuation — ELON/USDT P21_26

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.1829 |
| net_win_rate | 0.3470 |
| gross_profit_factor | 0.5722 |
| gross_win_rate | 0.3799 |
| sharpe_ratio | -13.5834 |
| sortino_ratio | -6.3359 |
| max_drawdown | 0.9997 |
| cagr | -0.9630 |
| net_avg_win | 6.4300 |
| net_avg_loss | -18.6795 |
| avg_hold_time_bars | 2.1834 |
| exposure | 0.0995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
