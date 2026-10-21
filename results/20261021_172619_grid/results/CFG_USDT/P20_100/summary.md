# EMA Hourly Continuation — CFG/USDT P20_100

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7380 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8874 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -1.9391 |
| sortino_ratio | -0.5484 |
| max_drawdown | 0.4973 |
| cagr | -0.2232 |
| net_avg_win | 71.5107 |
| net_avg_loss | -84.9549 |
| avg_hold_time_bars | 28.2323 |
| exposure | 0.5082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
