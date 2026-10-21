# EMA Hourly Continuation — BDX/USDT P21_55

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.4387 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.7192 |
| gross_win_rate | 0.4094 |
| sharpe_ratio | -4.7358 |
| sortino_ratio | -1.2132 |
| max_drawdown | 0.7728 |
| cagr | -0.4337 |
| net_avg_win | 45.3550 |
| net_avg_loss | -71.6569 |
| avg_hold_time_bars | 9.6031 |
| exposure | 0.1397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
