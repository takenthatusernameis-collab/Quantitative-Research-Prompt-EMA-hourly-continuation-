# EMA Hourly Continuation — CETUS/USDT P26_144

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7825 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0669 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -1.9176 |
| sortino_ratio | -0.5927 |
| max_drawdown | 0.5533 |
| cagr | -0.2441 |
| net_avg_win | 75.6133 |
| net_avg_loss | -99.5171 |
| avg_hold_time_bars | 23.3032 |
| exposure | 0.5009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
