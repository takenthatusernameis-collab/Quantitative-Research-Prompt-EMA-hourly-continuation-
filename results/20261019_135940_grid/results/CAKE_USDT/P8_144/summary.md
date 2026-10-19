# EMA Hourly Continuation — CAKE/USDT P8_144

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5875 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -3.9862 |
| sortino_ratio | -1.2670 |
| max_drawdown | 0.8089 |
| cagr | -0.4601 |
| net_avg_win | 47.5068 |
| net_avg_loss | -68.1593 |
| avg_hold_time_bars | 31.0136 |
| exposure | 0.7274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
