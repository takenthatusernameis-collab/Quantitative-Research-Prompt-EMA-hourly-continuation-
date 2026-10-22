# EMA Hourly Continuation — FLOKI/USDT P20_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.6748 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -3.1273 |
| sortino_ratio | -1.0969 |
| max_drawdown | 0.7506 |
| cagr | -0.4066 |
| net_avg_win | 49.6878 |
| net_avg_loss | -71.2949 |
| avg_hold_time_bars | 16.7629 |
| exposure | 0.4724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
