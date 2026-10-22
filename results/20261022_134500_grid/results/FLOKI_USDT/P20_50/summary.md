# EMA Hourly Continuation — FLOKI/USDT P20_50

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.5236 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8511 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -7.8038 |
| sortino_ratio | -3.6090 |
| max_drawdown | 0.9898 |
| cagr | -0.8341 |
| net_avg_win | 22.4559 |
| net_avg_loss | -34.1989 |
| avg_hold_time_bars | 4.4088 |
| exposure | 0.2186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
