# EMA Hourly Continuation — ZPAY/USDT P20_26

**Symbol:** ZPAY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.3133 |
| net_win_rate | 0.3175 |
| gross_profit_factor | 0.6462 |
| gross_win_rate | 0.3312 |
| sharpe_ratio | -11.1744 |
| sortino_ratio | -4.8226 |
| max_drawdown | 0.9975 |
| cagr | -0.9064 |
| net_avg_win | 15.1157 |
| net_avg_loss | -22.4489 |
| avg_hold_time_bars | 5.2437 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
