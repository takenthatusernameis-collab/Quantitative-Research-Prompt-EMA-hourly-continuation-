# EMA Hourly Continuation — NOT/USDT P20_100

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.8540 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0278 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -0.9398 |
| sortino_ratio | -0.2859 |
| max_drawdown | 0.3113 |
| cagr | -0.1260 |
| net_avg_win | 73.5301 |
| net_avg_loss | -90.1620 |
| avg_hold_time_bars | 19.4585 |
| exposure | 0.3967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
