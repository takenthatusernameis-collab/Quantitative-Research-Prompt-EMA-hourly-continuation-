# EMA Hourly Continuation — MINA/USDT P12_55

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -5.0601 |
| sortino_ratio | -2.1929 |
| max_drawdown | 0.9388 |
| cagr | -0.6527 |
| net_avg_win | 34.5184 |
| net_avg_loss | -50.7873 |
| avg_hold_time_bars | 9.7766 |
| exposure | 0.4217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
