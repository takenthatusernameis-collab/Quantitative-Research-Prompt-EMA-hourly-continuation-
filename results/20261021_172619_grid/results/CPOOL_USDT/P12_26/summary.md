# EMA Hourly Continuation — CPOOL/USDT P12_26

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.8513 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0741 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.1730 |
| sortino_ratio | -0.3454 |
| max_drawdown | 0.4293 |
| cagr | -0.1490 |
| net_avg_win | 88.3300 |
| net_avg_loss | -109.8598 |
| avg_hold_time_bars | 5.5429 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
