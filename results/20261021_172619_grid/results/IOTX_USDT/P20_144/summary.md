# EMA Hourly Continuation — IOTX/USDT P20_144

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.8059 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.2865 |
| sortino_ratio | -0.3849 |
| max_drawdown | 0.3874 |
| cagr | -0.1637 |
| net_avg_win | 67.9459 |
| net_avg_loss | -86.6641 |
| avg_hold_time_bars | 24.6881 |
| exposure | 0.4893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
