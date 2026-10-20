# EMA Hourly Continuation — CSPR/USDT P26_50

**Symbol:** CSPR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.3071 |
| net_win_rate | 0.3768 |
| gross_profit_factor | 0.7044 |
| gross_win_rate | 0.3960 |
| sharpe_ratio | -11.8562 |
| sortino_ratio | -5.9170 |
| max_drawdown | 0.9995 |
| cagr | -0.9521 |
| net_avg_win | 9.4057 |
| net_avg_loss | -18.5176 |
| avg_hold_time_bars | 2.9552 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
