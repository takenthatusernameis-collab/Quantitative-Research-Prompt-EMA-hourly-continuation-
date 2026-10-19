# EMA Hourly Continuation — BDX/USDT P100_200

**Symbol:** BDX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.2436 |
| net_win_rate | 0.3146 |
| gross_profit_factor | 0.6024 |
| gross_win_rate | 0.3615 |
| sharpe_ratio | -13.7464 |
| sortino_ratio | -5.9210 |
| max_drawdown | 0.9998 |
| cagr | -0.9634 |
| net_avg_win | 12.0161 |
| net_avg_loss | -22.6333 |
| avg_hold_time_bars | 4.8263 |
| exposure | 0.1869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
