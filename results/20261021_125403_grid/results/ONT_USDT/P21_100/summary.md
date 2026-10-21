# EMA Hourly Continuation — ONT/USDT P21_100

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.3687 |
| sortino_ratio | -0.7339 |
| max_drawdown | 0.6018 |
| cagr | -0.2871 |
| net_avg_win | 64.3665 |
| net_avg_loss | -79.9987 |
| avg_hold_time_bars | 18.6639 |
| exposure | 0.4020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
