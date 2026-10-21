# EMA Hourly Continuation — SHIB/USDT P12_50

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7394 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9995 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.5066 |
| sortino_ratio | -0.8825 |
| max_drawdown | 0.6551 |
| cagr | -0.3323 |
| net_avg_win | 60.4950 |
| net_avg_loss | -80.4665 |
| avg_hold_time_bars | 10.3781 |
| exposure | 0.2845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
