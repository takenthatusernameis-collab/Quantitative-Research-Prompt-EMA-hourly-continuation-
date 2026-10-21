# EMA Hourly Continuation — SKY/USDT P34_100

**Symbol:** SKY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7814 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0292 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.6793 |
| sortino_ratio | -0.5023 |
| max_drawdown | 0.5044 |
| cagr | -0.2063 |
| net_avg_win | 74.8294 |
| net_avg_loss | -98.5014 |
| avg_hold_time_bars | 14.2535 |
| exposure | 0.2821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
