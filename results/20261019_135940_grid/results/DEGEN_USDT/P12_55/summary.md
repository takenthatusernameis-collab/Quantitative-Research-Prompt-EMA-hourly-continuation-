# EMA Hourly Continuation — DEGEN/USDT P12_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.6744 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -4.6458 |
| sortino_ratio | -2.0166 |
| max_drawdown | 0.9099 |
| cagr | -0.6171 |
| net_avg_win | 42.6431 |
| net_avg_loss | -54.7982 |
| avg_hold_time_bars | 8.8739 |
| exposure | 0.3846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
