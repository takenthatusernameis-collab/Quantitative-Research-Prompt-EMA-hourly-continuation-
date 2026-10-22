# EMA Hourly Continuation — EUL/USDT P12_20

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.5284 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7550 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -3.6410 |
| sortino_ratio | -1.0367 |
| max_drawdown | 0.7152 |
| cagr | -0.3789 |
| net_avg_win | 44.4074 |
| net_avg_loss | -66.3333 |
| avg_hold_time_bars | 5.8020 |
| exposure | 0.1052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
