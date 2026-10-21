# EMA Hourly Continuation — CAKE/USDT P8_21

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7505 |
| net_win_rate | 0.5245 |
| gross_profit_factor | 1.1154 |
| gross_win_rate | 0.5245 |
| sharpe_ratio | -2.2262 |
| sortino_ratio | -0.7545 |
| max_drawdown | 0.5993 |
| cagr | -0.2914 |
| net_avg_win | 60.2533 |
| net_avg_loss | -88.5581 |
| avg_hold_time_bars | 6.1143 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
