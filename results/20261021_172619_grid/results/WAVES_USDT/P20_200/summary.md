# EMA Hourly Continuation — WAVES/USDT P20_200

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7791 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.5114 |
| sortino_ratio | -0.4228 |
| max_drawdown | 0.4385 |
| cagr | -0.1785 |
| net_avg_win | 71.9362 |
| net_avg_loss | -91.8566 |
| avg_hold_time_bars | 33.2611 |
| exposure | 0.5790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
