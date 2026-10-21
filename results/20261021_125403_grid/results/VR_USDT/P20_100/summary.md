# EMA Hourly Continuation — VR/USDT P20_100

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6595 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8080 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -2.5202 |
| sortino_ratio | -0.6943 |
| max_drawdown | 0.5592 |
| cagr | -0.2758 |
| net_avg_win | 62.8900 |
| net_avg_loss | -78.0251 |
| avg_hold_time_bars | 20.7000 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
