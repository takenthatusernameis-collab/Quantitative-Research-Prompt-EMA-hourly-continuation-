# EMA Hourly Continuation — RLC/USDT P20_100

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.8424 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0730 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.1726 |
| sortino_ratio | -0.3806 |
| max_drawdown | 0.4288 |
| cagr | -0.1629 |
| net_avg_win | 72.3582 |
| net_avg_loss | -93.6417 |
| avg_hold_time_bars | 17.3392 |
| exposure | 0.4020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
