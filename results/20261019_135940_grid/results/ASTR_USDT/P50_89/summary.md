# EMA Hourly Continuation — ASTR/USDT P50_89

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5219 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 1.0294 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -4.8943 |
| sortino_ratio | -1.7079 |
| max_drawdown | 0.8823 |
| cagr | -0.5657 |
| net_avg_win | 32.1678 |
| net_avg_loss | -58.3049 |
| avg_hold_time_bars | 5.4894 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
