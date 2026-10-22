# EMA Hourly Continuation — FET/USDT P8_26

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1633 |
| net_profit_factor | 0.4946 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -9.2656 |
| sortino_ratio | -5.2611 |
| max_drawdown | 0.9985 |
| cagr | -0.9249 |
| net_avg_win | 13.3147 |
| net_avg_loss | -21.9777 |
| avg_hold_time_bars | 3.4091 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
