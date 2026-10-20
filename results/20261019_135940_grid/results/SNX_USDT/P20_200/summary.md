# EMA Hourly Continuation — SNX/USDT P20_200

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.7666 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0551 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.8955 |
| sortino_ratio | -0.5537 |
| max_drawdown | 0.4885 |
| cagr | -0.2288 |
| net_avg_win | 73.7783 |
| net_avg_loss | -98.0781 |
| avg_hold_time_bars | 30.9387 |
| exposure | 0.5936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
