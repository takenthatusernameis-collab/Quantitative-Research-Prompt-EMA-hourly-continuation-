# EMA Hourly Continuation — KAVA/USDT P55_200

**Symbol:** KAVA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.6445 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.4889 |
| sortino_ratio | -0.5975 |
| max_drawdown | 0.5195 |
| cagr | -0.2475 |
| net_avg_win | 68.0365 |
| net_avg_loss | -92.6253 |
| avg_hold_time_bars | 29.9553 |
| exposure | 0.3962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
