# EMA Hourly Continuation — NYM/USDT P89_100

**Symbol:** NYM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.2691 |
| net_win_rate | 0.3273 |
| gross_profit_factor | 0.5208 |
| gross_win_rate | 0.3455 |
| sharpe_ratio | -3.7438 |
| sortino_ratio | -0.5655 |
| max_drawdown | 0.4969 |
| cagr | -0.2393 |
| net_avg_win | 50.8213 |
| net_avg_loss | -91.8748 |
| avg_hold_time_bars | 10.6000 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
