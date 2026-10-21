# EMA Hourly Continuation — DOT/USDT P20_200

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.9585 |
| net_win_rate | 0.5378 |
| gross_profit_factor | 1.1514 |
| gross_win_rate | 0.5378 |
| sharpe_ratio | -0.1585 |
| sortino_ratio | -0.0353 |
| max_drawdown | 0.1845 |
| cagr | -0.0200 |
| net_avg_win | 89.2104 |
| net_avg_loss | -108.3054 |
| avg_hold_time_bars | 63.1597 |
| exposure | 0.6833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
