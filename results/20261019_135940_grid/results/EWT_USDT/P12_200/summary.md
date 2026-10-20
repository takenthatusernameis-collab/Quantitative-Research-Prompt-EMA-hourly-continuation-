# EMA Hourly Continuation — EWT/USDT P12_200

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5388 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7660 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -4.3245 |
| sortino_ratio | -1.3808 |
| max_drawdown | 0.8421 |
| cagr | -0.4906 |
| net_avg_win | 41.6451 |
| net_avg_loss | -59.1943 |
| avg_hold_time_bars | 25.1970 |
| exposure | 0.6047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
