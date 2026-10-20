# EMA Hourly Continuation — OSMO/USDT P21_50

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.4580 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -8.1732 |
| sortino_ratio | -3.5252 |
| max_drawdown | 0.9878 |
| cagr | -0.8255 |
| net_avg_win | 21.1232 |
| net_avg_loss | -33.6764 |
| avg_hold_time_bars | 5.5139 |
| exposure | 0.2346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
