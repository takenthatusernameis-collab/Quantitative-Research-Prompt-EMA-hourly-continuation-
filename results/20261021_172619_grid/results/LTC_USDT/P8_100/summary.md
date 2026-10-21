# EMA Hourly Continuation — LTC/USDT P8_100

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6760 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.6617 |
| sortino_ratio | -0.7992 |
| max_drawdown | 0.6230 |
| cagr | -0.3081 |
| net_avg_win | 60.2501 |
| net_avg_loss | -79.2613 |
| avg_hold_time_bars | 32.0315 |
| exposure | 0.6465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
