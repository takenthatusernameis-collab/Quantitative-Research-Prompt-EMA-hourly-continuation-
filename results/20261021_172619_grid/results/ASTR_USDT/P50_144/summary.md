# EMA Hourly Continuation — ASTR/USDT P50_144

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9823 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.9497 |
| sortino_ratio | -0.5339 |
| max_drawdown | 0.4900 |
| cagr | -0.2186 |
| net_avg_win | 69.2735 |
| net_avg_loss | -92.6870 |
| avg_hold_time_bars | 16.3696 |
| exposure | 0.2726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
