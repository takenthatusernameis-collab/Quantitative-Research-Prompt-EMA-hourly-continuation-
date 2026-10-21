# EMA Hourly Continuation — ASTR/USDT P21_89

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8084 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0878 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -1.6243 |
| sortino_ratio | -0.5163 |
| max_drawdown | 0.4914 |
| cagr | -0.2137 |
| net_avg_win | 74.9304 |
| net_avg_loss | -99.2857 |
| avg_hold_time_bars | 17.3737 |
| exposure | 0.3892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
