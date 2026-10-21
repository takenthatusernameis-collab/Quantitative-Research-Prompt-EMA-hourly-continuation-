# EMA Hourly Continuation — AERO/USDT P8_12

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.7545 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.2305 |
| sortino_ratio | -0.2737 |
| max_drawdown | 0.3198 |
| cagr | -0.1173 |
| net_avg_win | 67.7715 |
| net_avg_loss | -93.6645 |
| avg_hold_time_bars | 4.3431 |
| exposure | 0.0472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
