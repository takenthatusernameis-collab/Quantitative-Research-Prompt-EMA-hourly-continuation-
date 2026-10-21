# EMA Hourly Continuation — AIOZ/USDT P21_26

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 158 |
| net_profit_factor | 0.5196 |
| net_win_rate | 0.3987 |
| gross_profit_factor | 0.6833 |
| gross_win_rate | 0.3987 |
| sharpe_ratio | -2.6686 |
| sortino_ratio | -0.4749 |
| max_drawdown | 0.4468 |
| cagr | -0.1973 |
| net_avg_win | 72.8093 |
| net_avg_loss | -92.9236 |
| avg_hold_time_bars | 5.3987 |
| exposure | 0.0388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
