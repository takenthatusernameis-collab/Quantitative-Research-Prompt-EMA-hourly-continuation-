# EMA Hourly Continuation — IOTX/USDT P12_34

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7809 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0726 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.8070 |
| sortino_ratio | -0.6378 |
| max_drawdown | 0.5572 |
| cagr | -0.2534 |
| net_avg_win | 59.1932 |
| net_avg_loss | -82.9611 |
| avg_hold_time_bars | 7.3706 |
| exposure | 0.2007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
