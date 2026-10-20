# EMA Hourly Continuation — GTC/USDT P26_50

**Symbol:** GTC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.4586 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -7.8309 |
| sortino_ratio | -3.3364 |
| max_drawdown | 0.9843 |
| cagr | -0.8056 |
| net_avg_win | 21.1979 |
| net_avg_loss | -34.6701 |
| avg_hold_time_bars | 4.5202 |
| exposure | 0.1884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
