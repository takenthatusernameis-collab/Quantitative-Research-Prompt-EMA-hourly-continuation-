# EMA Hourly Continuation — FLIP/USDT P21_200

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -1.6709 |
| sortino_ratio | -0.3904 |
| max_drawdown | 0.4071 |
| cagr | -0.1667 |
| net_avg_win | 69.0681 |
| net_avg_loss | -87.3950 |
| avg_hold_time_bars | 49.0696 |
| exposure | 0.6089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
