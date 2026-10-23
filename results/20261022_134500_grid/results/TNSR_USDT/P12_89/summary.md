# EMA Hourly Continuation — TNSR/USDT P12_89

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.7255 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -3.4277 |
| sortino_ratio | -1.3271 |
| max_drawdown | 0.8141 |
| cagr | -0.4677 |
| net_avg_win | 57.4889 |
| net_avg_loss | -73.6099 |
| avg_hold_time_bars | 15.5605 |
| exposure | 0.5352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
