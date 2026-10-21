# EMA Hourly Continuation — DYDX/USDT P20_144

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8526 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -0.9222 |
| sortino_ratio | -0.2454 |
| max_drawdown | 0.3018 |
| cagr | -0.1088 |
| net_avg_win | 83.4873 |
| net_avg_loss | -99.0596 |
| avg_hold_time_bars | 36.4046 |
| exposure | 0.5725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
