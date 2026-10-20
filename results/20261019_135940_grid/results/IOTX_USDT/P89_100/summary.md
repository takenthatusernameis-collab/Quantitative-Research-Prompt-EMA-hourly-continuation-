# EMA Hourly Continuation — IOTX/USDT P89_100

**Symbol:** IOTX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.2927 |
| net_win_rate | 0.3947 |
| gross_profit_factor | 0.8053 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -9.8164 |
| sortino_ratio | -3.7076 |
| max_drawdown | 0.9935 |
| cagr | -0.8634 |
| net_avg_win | 15.3358 |
| net_avg_loss | -34.1668 |
| avg_hold_time_bars | 1.9735 |
| exposure | 0.0609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
