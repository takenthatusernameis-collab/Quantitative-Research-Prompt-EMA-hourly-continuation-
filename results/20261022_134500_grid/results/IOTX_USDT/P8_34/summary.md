# EMA Hourly Continuation — IOTX/USDT P8_34

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1321 |
| net_profit_factor | 0.5441 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -7.6197 |
| sortino_ratio | -3.8947 |
| max_drawdown | 0.9917 |
| cagr | -0.8516 |
| net_avg_win | 18.9689 |
| net_avg_loss | -31.2102 |
| avg_hold_time_bars | 6.1726 |
| exposure | 0.3706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
