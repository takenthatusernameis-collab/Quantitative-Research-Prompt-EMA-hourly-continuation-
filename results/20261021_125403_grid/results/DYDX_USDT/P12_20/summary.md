# EMA Hourly Continuation — DYDX/USDT P12_20

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6872 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.0631 |
| sortino_ratio | -0.5064 |
| max_drawdown | 0.4404 |
| cagr | -0.2064 |
| net_avg_win | 68.1252 |
| net_avg_loss | -92.6142 |
| avg_hold_time_bars | 5.1156 |
| exposure | 0.0684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
