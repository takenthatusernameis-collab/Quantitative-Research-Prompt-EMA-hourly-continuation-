# EMA Hourly Continuation — POLYX/USDT P8_200

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0079 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.6504 |
| sortino_ratio | -0.4424 |
| max_drawdown | 0.4466 |
| cagr | -0.1872 |
| net_avg_win | 66.7780 |
| net_avg_loss | -90.0858 |
| avg_hold_time_bars | 49.4535 |
| exposure | 0.7980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
