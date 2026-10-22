# EMA Hourly Continuation — INJ/USDT P8_12

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1847 |
| net_profit_factor | 0.1828 |
| net_win_rate | 0.3655 |
| gross_profit_factor | 0.5146 |
| gross_win_rate | 0.3985 |
| sharpe_ratio | -17.6772 |
| sortino_ratio | -10.9287 |
| max_drawdown | 1.0000 |
| cagr | -0.9972 |
| net_avg_win | 3.3148 |
| net_avg_loss | -10.4415 |
| avg_hold_time_bars | 1.7060 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
