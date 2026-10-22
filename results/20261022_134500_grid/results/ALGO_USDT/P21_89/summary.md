# EMA Hourly Continuation — ALGO/USDT P21_89

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6226 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -4.1771 |
| sortino_ratio | -1.5547 |
| max_drawdown | 0.8589 |
| cagr | -0.5302 |
| net_avg_win | 41.3590 |
| net_avg_loss | -61.5332 |
| avg_hold_time_bars | 11.0823 |
| exposure | 0.3551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
