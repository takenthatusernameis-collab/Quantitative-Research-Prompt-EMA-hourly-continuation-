# EMA Hourly Continuation — MNT/USDT P20_50

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -2.5469 |
| sortino_ratio | -0.8268 |
| max_drawdown | 0.6304 |
| cagr | -0.3140 |
| net_avg_win | 51.4261 |
| net_avg_loss | -77.4412 |
| avg_hold_time_bars | 9.2902 |
| exposure | 0.2154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
