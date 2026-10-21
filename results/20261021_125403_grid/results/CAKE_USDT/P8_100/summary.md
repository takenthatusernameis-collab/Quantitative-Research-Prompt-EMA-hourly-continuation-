# EMA Hourly Continuation — CAKE/USDT P8_100

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.8356 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0600 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.2767 |
| sortino_ratio | -0.3982 |
| max_drawdown | 0.4386 |
| cagr | -0.1695 |
| net_avg_win | 77.9887 |
| net_avg_loss | -98.6074 |
| avg_hold_time_bars | 30.5497 |
| exposure | 0.6568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
