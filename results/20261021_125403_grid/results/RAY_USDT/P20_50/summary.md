# EMA Hourly Continuation — RAY/USDT P20_50

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.7871 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0164 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.9935 |
| sortino_ratio | -0.6531 |
| max_drawdown | 0.6218 |
| cagr | -0.2604 |
| net_avg_win | 75.2408 |
| net_avg_loss | -94.8631 |
| avg_hold_time_bars | 7.7233 |
| exposure | 0.1840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
