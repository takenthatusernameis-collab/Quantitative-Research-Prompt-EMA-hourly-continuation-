# EMA Hourly Continuation — POLYX/USDT P21_89

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6644 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.8719 |
| sortino_ratio | -1.4347 |
| max_drawdown | 0.8391 |
| cagr | -0.4960 |
| net_avg_win | 48.5260 |
| net_avg_loss | -67.9641 |
| avg_hold_time_bars | 11.6604 |
| exposure | 0.3684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
