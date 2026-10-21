# EMA Hourly Continuation — G/USDT P20_100

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.7151 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -3.5605 |
| sortino_ratio | -1.0523 |
| max_drawdown | 0.6851 |
| cagr | -0.3850 |
| net_avg_win | 50.8997 |
| net_avg_loss | -68.1201 |
| avg_hold_time_bars | 25.6419 |
| exposure | 0.5083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
