# EMA Hourly Continuation — BLZ/USDT P12_100

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.8384 |
| gross_win_rate | 0.4309 |
| sharpe_ratio | -5.7397 |
| sortino_ratio | -2.1842 |
| max_drawdown | 0.9348 |
| cagr | -0.6535 |
| net_avg_win | 41.0961 |
| net_avg_loss | -52.6274 |
| avg_hold_time_bars | 16.3893 |
| exposure | 0.5526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
