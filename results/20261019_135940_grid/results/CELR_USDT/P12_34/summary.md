# EMA Hourly Continuation — CELR/USDT P12_34

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.4656 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -8.7486 |
| sortino_ratio | -4.3061 |
| max_drawdown | 0.9948 |
| cagr | -0.8751 |
| net_avg_win | 16.7283 |
| net_avg_loss | -26.7039 |
| avg_hold_time_bars | 4.8979 |
| exposure | 0.2693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
