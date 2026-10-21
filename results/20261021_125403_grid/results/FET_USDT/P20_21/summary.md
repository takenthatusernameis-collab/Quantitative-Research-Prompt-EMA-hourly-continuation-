# EMA Hourly Continuation — FET/USDT P20_21

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 89 |
| net_profit_factor | 0.8274 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0658 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.5477 |
| sortino_ratio | -0.0744 |
| max_drawdown | 0.1459 |
| cagr | -0.0338 |
| net_avg_win | 86.2692 |
| net_avg_loss | -111.5361 |
| avg_hold_time_bars | 5.0225 |
| exposure | 0.0203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
