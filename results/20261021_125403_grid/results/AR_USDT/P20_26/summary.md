# EMA Hourly Continuation — AR/USDT P20_26

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.5549 |
| net_win_rate | 0.4294 |
| gross_profit_factor | 0.7538 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -2.4084 |
| sortino_ratio | -0.4465 |
| max_drawdown | 0.4153 |
| cagr | -0.1864 |
| net_avg_win | 69.0592 |
| net_avg_loss | -93.6611 |
| avg_hold_time_bars | 5.3235 |
| exposure | 0.0411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
