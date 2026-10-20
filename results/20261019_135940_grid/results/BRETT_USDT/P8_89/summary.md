# EMA Hourly Continuation — BRETT/USDT P8_89

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.7060 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.2715 |
| sortino_ratio | -1.2326 |
| max_drawdown | 0.7520 |
| cagr | -0.4438 |
| net_avg_win | 56.0222 |
| net_avg_loss | -71.7761 |
| avg_hold_time_bars | 19.6504 |
| exposure | 0.6411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
