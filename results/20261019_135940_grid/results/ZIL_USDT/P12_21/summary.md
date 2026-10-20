# EMA Hourly Continuation — ZIL/USDT P12_21

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.2495 |
| net_win_rate | 0.3910 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -14.3903 |
| sortino_ratio | -7.9990 |
| max_drawdown | 1.0000 |
| cagr | -0.9841 |
| net_avg_win | 5.7203 |
| net_avg_loss | -14.7218 |
| avg_hold_time_bars | 2.3594 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
