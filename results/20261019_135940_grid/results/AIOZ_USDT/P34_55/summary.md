# EMA Hourly Continuation — AIOZ/USDT P34_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.5847 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -8.0773 |
| sortino_ratio | -3.5610 |
| max_drawdown | 0.9882 |
| cagr | -0.8271 |
| net_avg_win | 32.5670 |
| net_avg_loss | -43.4812 |
| avg_hold_time_bars | 3.3398 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
