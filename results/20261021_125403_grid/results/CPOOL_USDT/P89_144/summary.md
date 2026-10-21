# EMA Hourly Continuation — CPOOL/USDT P89_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.6699 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -2.0391 |
| sortino_ratio | -0.4721 |
| max_drawdown | 0.4712 |
| cagr | -0.1958 |
| net_avg_win | 70.6923 |
| net_avg_loss | -88.0561 |
| avg_hold_time_bars | 7.6992 |
| exposure | 0.0931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
