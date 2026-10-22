# EMA Hourly Continuation — FLOKI/USDT P20_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.3226 |
| sortino_ratio | -0.6157 |
| max_drawdown | 0.5306 |
| cagr | -0.2514 |
| net_avg_win | 64.1415 |
| net_avg_loss | -85.3730 |
| avg_hold_time_bars | 41.5949 |
| exposure | 0.6674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
