# EMA Hourly Continuation — G/USDT P26_100

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.5431 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.8511 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -4.7736 |
| sortino_ratio | -1.6355 |
| max_drawdown | 0.8338 |
| cagr | -0.5413 |
| net_avg_win | 43.2930 |
| net_avg_loss | -61.9999 |
| avg_hold_time_bars | 15.3594 |
| exposure | 0.4135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
