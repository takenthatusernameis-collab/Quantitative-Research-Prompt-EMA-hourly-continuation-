# EMA Hourly Continuation — BICO/USDT P8_200

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.9398 |
| net_win_rate | 0.5230 |
| gross_profit_factor | 1.0828 |
| gross_win_rate | 0.5230 |
| sharpe_ratio | -0.2804 |
| sortino_ratio | -0.0703 |
| max_drawdown | 0.2293 |
| cagr | -0.0364 |
| net_avg_win | 87.3095 |
| net_avg_loss | -101.8706 |
| avg_hold_time_bars | 57.1447 |
| exposure | 0.7896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
