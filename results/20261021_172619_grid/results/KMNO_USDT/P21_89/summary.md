# EMA Hourly Continuation — KMNO/USDT P21_89

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7297 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -2.0386 |
| sortino_ratio | -0.6006 |
| max_drawdown | 0.5274 |
| cagr | -0.2430 |
| net_avg_win | 66.8478 |
| net_avg_loss | -83.3156 |
| avg_hold_time_bars | 18.1967 |
| exposure | 0.3545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
