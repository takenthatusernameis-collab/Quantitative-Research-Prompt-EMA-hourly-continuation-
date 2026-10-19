# EMA Hourly Continuation — DOT/USDT P8_50

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9944 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -6.1321 |
| sortino_ratio | -2.7958 |
| max_drawdown | 0.9706 |
| cagr | -0.7456 |
| net_avg_win | 25.3869 |
| net_avg_loss | -40.2300 |
| avg_hold_time_bars | 9.9585 |
| exposure | 0.4803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
