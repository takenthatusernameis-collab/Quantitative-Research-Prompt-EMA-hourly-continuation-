# EMA Hourly Continuation — TRAC/USDT P20_55

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.7857 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -1.6431 |
| sortino_ratio | -0.5254 |
| max_drawdown | 0.4932 |
| cagr | -0.2143 |
| net_avg_win | 66.0966 |
| net_avg_loss | -86.8843 |
| avg_hold_time_bars | 10.3004 |
| exposure | 0.2322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
