# EMA Hourly Continuation — DYDX/USDT P12_200

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.8889 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -0.4918 |
| sortino_ratio | -0.1031 |
| max_drawdown | 0.1585 |
| cagr | -0.0484 |
| net_avg_win | 85.2325 |
| net_avg_loss | -101.4142 |
| avg_hold_time_bars | 83.2430 |
| exposure | 0.8097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
