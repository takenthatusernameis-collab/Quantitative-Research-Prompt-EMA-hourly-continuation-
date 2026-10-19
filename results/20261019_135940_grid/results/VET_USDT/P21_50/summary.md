# EMA Hourly Continuation — VET/USDT P21_50

**Symbol:** VET/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.4957 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -7.6737 |
| sortino_ratio | -3.4111 |
| max_drawdown | 0.9873 |
| cagr | -0.8216 |
| net_avg_win | 20.8187 |
| net_avg_loss | -36.3076 |
| avg_hold_time_bars | 4.1751 |
| exposure | 0.1907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
