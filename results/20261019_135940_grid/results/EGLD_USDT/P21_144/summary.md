# EMA Hourly Continuation — EGLD/USDT P21_144

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.5992 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -3.0737 |
| sortino_ratio | -0.9730 |
| max_drawdown | 0.7074 |
| cagr | -0.3748 |
| net_avg_win | 41.7519 |
| net_avg_loss | -66.4624 |
| avg_hold_time_bars | 22.9606 |
| exposure | 0.5302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
