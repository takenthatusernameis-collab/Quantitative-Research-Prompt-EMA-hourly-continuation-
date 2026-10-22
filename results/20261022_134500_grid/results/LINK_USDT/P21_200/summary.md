# EMA Hourly Continuation — LINK/USDT P21_200

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6606 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0611 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -2.6049 |
| sortino_ratio | -0.7389 |
| max_drawdown | 0.6183 |
| cagr | -0.3016 |
| net_avg_win | 55.8527 |
| net_avg_loss | -85.3741 |
| avg_hold_time_bars | 30.2816 |
| exposure | 0.5671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
