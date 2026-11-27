# EMA Hourly Continuation — SHR/USDT P21_50

**Symbol:** SHR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.3710 |
| net_win_rate | 0.3163 |
| gross_profit_factor | 0.5903 |
| gross_win_rate | 0.3195 |
| sharpe_ratio | -12.2078 |
| sortino_ratio | -6.0103 |
| max_drawdown | 0.9994 |
| cagr | -0.9468 |
| net_avg_win | 15.1173 |
| net_avg_loss | -18.8489 |
| avg_hold_time_bars | 3.9254 |
| exposure | 0.2190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
