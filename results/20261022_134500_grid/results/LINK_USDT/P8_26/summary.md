# EMA Hourly Continuation — LINK/USDT P8_26

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1520 |
| net_profit_factor | 0.4140 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.9256 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -10.8404 |
| sortino_ratio | -5.9277 |
| max_drawdown | 0.9995 |
| cagr | -0.9515 |
| net_avg_win | 10.5235 |
| net_avg_loss | -20.0898 |
| avg_hold_time_bars | 3.7112 |
| exposure | 0.2564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
