# EMA Hourly Continuation — PYTH/USDT P26_100

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.1123 |
| sortino_ratio | -0.6287 |
| max_drawdown | 0.5440 |
| cagr | -0.2514 |
| net_avg_win | 68.0812 |
| net_avg_loss | -82.0741 |
| avg_hold_time_bars | 15.0708 |
| exposure | 0.3000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
