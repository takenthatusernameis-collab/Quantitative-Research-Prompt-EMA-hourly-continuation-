# EMA Hourly Continuation — SLP/USDT P89_200

**Symbol:** SLP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8510 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0925 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -0.8448 |
| sortino_ratio | -0.2128 |
| max_drawdown | 0.2296 |
| cagr | -0.0949 |
| net_avg_win | 79.0428 |
| net_avg_loss | -101.7919 |
| avg_hold_time_bars | 14.3987 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
