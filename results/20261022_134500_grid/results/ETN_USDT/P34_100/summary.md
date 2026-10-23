# EMA Hourly Continuation — ETN/USDT P34_100

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.3665 |
| net_win_rate | 0.3667 |
| gross_profit_factor | 0.5802 |
| gross_win_rate | 0.3790 |
| sharpe_ratio | -8.6460 |
| sortino_ratio | -3.3980 |
| max_drawdown | 0.9712 |
| cagr | -0.8137 |
| net_avg_win | 23.6010 |
| net_avg_loss | -37.2857 |
| avg_hold_time_bars | 7.4022 |
| exposure | 0.2609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
