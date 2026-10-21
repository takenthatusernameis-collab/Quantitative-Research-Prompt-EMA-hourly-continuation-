# EMA Hourly Continuation — ENA/USDT P26_55

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8136 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.3410 |
| sortino_ratio | -0.3913 |
| max_drawdown | 0.4158 |
| cagr | -0.1657 |
| net_avg_win | 77.0860 |
| net_avg_loss | -94.2912 |
| avg_hold_time_bars | 7.9036 |
| exposure | 0.1491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
