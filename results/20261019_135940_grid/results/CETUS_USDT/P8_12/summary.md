# EMA Hourly Continuation — CETUS/USDT P8_12

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1784 |
| net_profit_factor | 0.2785 |
| net_win_rate | 0.3890 |
| gross_profit_factor | 0.8056 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -15.1867 |
| sortino_ratio | -9.1464 |
| max_drawdown | 1.0000 |
| cagr | -0.9911 |
| net_avg_win | 5.5624 |
| net_avg_loss | -12.7158 |
| avg_hold_time_bars | 1.9933 |
| exposure | 0.1609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
