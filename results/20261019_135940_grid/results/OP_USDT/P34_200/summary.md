# EMA Hourly Continuation — OP/USDT P34_200

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7400 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0476 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.7043 |
| sortino_ratio | -0.4474 |
| max_drawdown | 0.4338 |
| cagr | -0.1893 |
| net_avg_win | 67.7595 |
| net_avg_loss | -92.1060 |
| avg_hold_time_bars | 34.9184 |
| exposure | 0.5444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
