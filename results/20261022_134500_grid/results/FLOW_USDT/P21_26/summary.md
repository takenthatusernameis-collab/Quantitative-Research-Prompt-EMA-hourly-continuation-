# EMA Hourly Continuation — FLOW/USDT P21_26

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.2223 |
| net_win_rate | 0.3495 |
| gross_profit_factor | 0.7701 |
| gross_win_rate | 0.4061 |
| sharpe_ratio | -15.4920 |
| sortino_ratio | -7.9481 |
| max_drawdown | 1.0000 |
| cagr | -0.9857 |
| net_avg_win | 6.7094 |
| net_avg_loss | -16.2143 |
| avg_hold_time_bars | 1.9188 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
