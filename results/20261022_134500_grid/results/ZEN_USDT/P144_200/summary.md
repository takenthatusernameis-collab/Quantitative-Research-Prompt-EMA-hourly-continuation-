# EMA Hourly Continuation — ZEN/USDT P144_200

**Symbol:** ZEN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.4716 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9273 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -4.3328 |
| sortino_ratio | -1.2509 |
| max_drawdown | 0.7970 |
| cagr | -0.4637 |
| net_avg_win | 35.4635 |
| net_avg_loss | -66.8114 |
| avg_hold_time_bars | 4.1891 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
