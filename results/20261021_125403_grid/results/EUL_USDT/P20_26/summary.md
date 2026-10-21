# EMA Hourly Continuation — EUL/USDT P20_26

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.5441 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.7938 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -2.8346 |
| sortino_ratio | -0.6661 |
| max_drawdown | 0.5470 |
| cagr | -0.2640 |
| net_avg_win | 52.0994 |
| net_avg_loss | -80.1152 |
| avg_hold_time_bars | 6.0778 |
| exposure | 0.0746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
