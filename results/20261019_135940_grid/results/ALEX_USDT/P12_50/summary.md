# EMA Hourly Continuation — ALEX/USDT P12_50

**Symbol:** ALEX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.5788 |
| net_win_rate | 0.4180 |
| gross_profit_factor | 0.9955 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -7.3372 |
| sortino_ratio | -3.0913 |
| max_drawdown | 0.9821 |
| cagr | -0.7920 |
| net_avg_win | 35.0047 |
| net_avg_loss | -43.4383 |
| avg_hold_time_bars | 8.9729 |
| exposure | 0.3756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
