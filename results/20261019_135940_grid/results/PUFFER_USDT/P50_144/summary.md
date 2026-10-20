# EMA Hourly Continuation — PUFFER/USDT P50_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.5857 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8002 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -3.5274 |
| sortino_ratio | -1.1034 |
| max_drawdown | 0.6700 |
| cagr | -0.4081 |
| net_avg_win | 51.5535 |
| net_avg_loss | -71.6166 |
| avg_hold_time_bars | 12.3058 |
| exposure | 0.2779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
