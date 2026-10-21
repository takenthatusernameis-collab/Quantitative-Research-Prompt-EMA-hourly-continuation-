# EMA Hourly Continuation — SEI/USDT P21_89

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.8958 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0894 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.7005 |
| sortino_ratio | -0.2138 |
| max_drawdown | 0.3118 |
| cagr | -0.0977 |
| net_avg_win | 83.2592 |
| net_avg_loss | -102.0667 |
| avg_hold_time_bars | 18.4076 |
| exposure | 0.3757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
