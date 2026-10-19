# EMA Hourly Continuation — CVX/USDT P26_89

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -4.4250 |
| sortino_ratio | -1.6562 |
| max_drawdown | 0.8642 |
| cagr | -0.5467 |
| net_avg_win | 38.1535 |
| net_avg_loss | -55.1484 |
| avg_hold_time_bars | 8.9845 |
| exposure | 0.2891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
