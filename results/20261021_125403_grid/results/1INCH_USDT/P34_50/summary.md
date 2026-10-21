# EMA Hourly Continuation — 1INCH/USDT P34_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.5596 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8449 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -3.0731 |
| sortino_ratio | -0.7656 |
| max_drawdown | 0.5920 |
| cagr | -0.2958 |
| net_avg_win | 53.5370 |
| net_avg_loss | -81.5771 |
| avg_hold_time_bars | 4.9768 |
| exposure | 0.0683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
