# EMA Hourly Continuation — CAKE/USDT P8_100

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6036 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 1.0118 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -4.3544 |
| sortino_ratio | -1.5260 |
| max_drawdown | 0.8650 |
| cagr | -0.5339 |
| net_avg_win | 42.5827 |
| net_avg_loss | -64.4227 |
| avg_hold_time_bars | 23.0548 |
| exposure | 0.6696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
