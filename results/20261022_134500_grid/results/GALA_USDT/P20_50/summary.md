# EMA Hourly Continuation — GALA/USDT P20_50

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.4385 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.7700 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -8.1621 |
| sortino_ratio | -3.7645 |
| max_drawdown | 0.9900 |
| cagr | -0.8367 |
| net_avg_win | 17.2089 |
| net_avg_loss | -28.9347 |
| avg_hold_time_bars | 4.3091 |
| exposure | 0.2072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
