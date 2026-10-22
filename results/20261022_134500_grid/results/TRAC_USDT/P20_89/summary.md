# EMA Hourly Continuation — TRAC/USDT P20_89

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6584 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.9397 |
| sortino_ratio | -1.4905 |
| max_drawdown | 0.8415 |
| cagr | -0.5084 |
| net_avg_win | 46.8914 |
| net_avg_loss | -64.6048 |
| avg_hold_time_bars | 10.6259 |
| exposure | 0.3473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
