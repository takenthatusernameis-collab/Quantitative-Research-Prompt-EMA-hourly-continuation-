# EMA Hourly Continuation — UQC/USDT P8_26

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.1686 |
| net_win_rate | 0.2694 |
| gross_profit_factor | 0.4765 |
| gross_win_rate | 0.2988 |
| sharpe_ratio | -11.1485 |
| sortino_ratio | -3.8524 |
| max_drawdown | 0.9955 |
| cagr | -0.8815 |
| net_avg_win | 12.9429 |
| net_avg_loss | -28.3049 |
| avg_hold_time_bars | 23.0017 |
| exposure | 0.6028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
