# EMA Hourly Continuation — IMX/USDT P26_89

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -3.0965 |
| sortino_ratio | -1.1303 |
| max_drawdown | 0.7453 |
| cagr | -0.4147 |
| net_avg_win | 45.9165 |
| net_avg_loss | -66.5592 |
| avg_hold_time_bars | 10.6637 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
