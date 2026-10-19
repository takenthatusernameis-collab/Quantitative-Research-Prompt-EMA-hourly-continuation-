# EMA Hourly Continuation — BSV/USDT P34_200

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.5366 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8024 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -3.7666 |
| sortino_ratio | -1.0692 |
| max_drawdown | 0.7264 |
| cagr | -0.3966 |
| net_avg_win | 45.9822 |
| net_avg_loss | -67.7343 |
| avg_hold_time_bars | 28.4610 |
| exposure | 0.5304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
