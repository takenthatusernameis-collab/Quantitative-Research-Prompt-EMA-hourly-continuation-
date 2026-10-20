# EMA Hourly Continuation — BRETT/USDT P21_89

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6263 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -4.3819 |
| sortino_ratio | -1.6240 |
| max_drawdown | 0.8432 |
| cagr | -0.5377 |
| net_avg_win | 48.0278 |
| net_avg_loss | -61.5582 |
| avg_hold_time_bars | 11.7097 |
| exposure | 0.3707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
