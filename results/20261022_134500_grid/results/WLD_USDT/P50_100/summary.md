# EMA Hourly Continuation — WLD/USDT P50_100

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6740 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -2.9872 |
| sortino_ratio | -1.0084 |
| max_drawdown | 0.6982 |
| cagr | -0.3771 |
| net_avg_win | 51.5371 |
| net_avg_loss | -74.5922 |
| avg_hold_time_bars | 6.4619 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
