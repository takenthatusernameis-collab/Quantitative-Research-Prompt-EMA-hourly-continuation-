# EMA Hourly Continuation — LQTY/USDT P21_55

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -5.7663 |
| sortino_ratio | -2.4933 |
| max_drawdown | 0.9515 |
| cagr | -0.6970 |
| net_avg_win | 23.9801 |
| net_avg_loss | -39.8005 |
| avg_hold_time_bars | 6.5169 |
| exposure | 0.2784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
