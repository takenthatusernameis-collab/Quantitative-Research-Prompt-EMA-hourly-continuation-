# EMA Hourly Continuation — CPOOL/USDT P89_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.4515 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.6915 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -6.1298 |
| sortino_ratio | -2.0176 |
| max_drawdown | 0.9207 |
| cagr | -0.6294 |
| net_avg_win | 34.6434 |
| net_avg_loss | -50.6841 |
| avg_hold_time_bars | 4.8066 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
