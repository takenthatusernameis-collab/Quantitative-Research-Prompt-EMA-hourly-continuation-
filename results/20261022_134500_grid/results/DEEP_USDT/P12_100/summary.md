# EMA Hourly Continuation — DEEP/USDT P12_100

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0358 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -1.9596 |
| sortino_ratio | -0.6847 |
| max_drawdown | 0.5329 |
| cagr | -0.2761 |
| net_avg_win | 73.5040 |
| net_avg_loss | -93.8926 |
| avg_hold_time_bars | 21.7016 |
| exposure | 0.5972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
