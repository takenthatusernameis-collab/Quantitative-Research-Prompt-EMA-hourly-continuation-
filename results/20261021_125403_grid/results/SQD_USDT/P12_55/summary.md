# EMA Hourly Continuation — SQD/USDT P12_55

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.8582 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.1965 |
| sortino_ratio | -0.4250 |
| max_drawdown | 0.4511 |
| cagr | -0.1813 |
| net_avg_win | 77.3448 |
| net_avg_loss | -92.5903 |
| avg_hold_time_bars | 11.6919 |
| exposure | 0.3264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
