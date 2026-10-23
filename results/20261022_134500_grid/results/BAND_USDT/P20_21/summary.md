# EMA Hourly Continuation — BAND/USDT P20_21

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1139 |
| net_profit_factor | 0.1877 |
| net_win_rate | 0.3284 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -15.3132 |
| sortino_ratio | -7.6224 |
| max_drawdown | 1.0000 |
| cagr | -0.9852 |
| net_avg_win | 6.1774 |
| net_avg_loss | -16.0917 |
| avg_hold_time_bars | 2.3784 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
