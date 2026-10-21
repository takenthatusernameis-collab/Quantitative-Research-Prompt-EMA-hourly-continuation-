# EMA Hourly Continuation — ILV/USDT P20_26

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6918 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0406 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.6889 |
| sortino_ratio | -0.3730 |
| max_drawdown | 0.3707 |
| cagr | -0.1561 |
| net_avg_win | 64.3784 |
| net_avg_loss | -98.7795 |
| avg_hold_time_bars | 5.2255 |
| exposure | 0.0558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
