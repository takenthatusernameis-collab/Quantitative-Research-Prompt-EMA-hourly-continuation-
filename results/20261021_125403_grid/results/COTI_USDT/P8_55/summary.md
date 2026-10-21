# EMA Hourly Continuation — COTI/USDT P8_55

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.8535 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0348 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.4605 |
| sortino_ratio | -0.5614 |
| max_drawdown | 0.5384 |
| cagr | -0.2309 |
| net_avg_win | 77.2846 |
| net_avg_loss | -92.8433 |
| avg_hold_time_bars | 13.6231 |
| exposure | 0.4452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
