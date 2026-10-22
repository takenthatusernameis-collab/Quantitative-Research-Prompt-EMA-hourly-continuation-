# EMA Hourly Continuation — JTO/USDT P21_34

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.4444 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8801 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -8.5277 |
| sortino_ratio | -4.0942 |
| max_drawdown | 0.9936 |
| cagr | -0.8654 |
| net_avg_win | 15.3997 |
| net_avg_loss | -28.1151 |
| avg_hold_time_bars | 2.8620 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
