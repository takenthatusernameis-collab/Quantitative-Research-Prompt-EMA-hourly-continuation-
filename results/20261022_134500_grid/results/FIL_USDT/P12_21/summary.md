# EMA Hourly Continuation — FIL/USDT P12_21

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1487 |
| net_profit_factor | 0.2219 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.6577 |
| gross_win_rate | 0.4169 |
| sharpe_ratio | -14.5996 |
| sortino_ratio | -8.0638 |
| max_drawdown | 1.0000 |
| cagr | -0.9856 |
| net_avg_win | 4.9070 |
| net_avg_loss | -14.1840 |
| avg_hold_time_bars | 2.1970 |
| exposure | 0.1485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
