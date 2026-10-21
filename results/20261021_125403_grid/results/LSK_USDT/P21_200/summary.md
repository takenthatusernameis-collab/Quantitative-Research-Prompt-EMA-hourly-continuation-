# EMA Hourly Continuation — LSK/USDT P21_200

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8039 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.2547 |
| sortino_ratio | -0.3280 |
| max_drawdown | 0.4143 |
| cagr | -0.1422 |
| net_avg_win | 77.5537 |
| net_avg_loss | -98.2166 |
| avg_hold_time_bars | 38.6687 |
| exposure | 0.5888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
