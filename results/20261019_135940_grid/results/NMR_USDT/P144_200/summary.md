# EMA Hourly Continuation — NMR/USDT P144_200

**Symbol:** NMR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.3844 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.7828 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -6.0888 |
| sortino_ratio | -1.8213 |
| max_drawdown | 0.9017 |
| cagr | -0.6008 |
| net_avg_win | 29.7458 |
| net_avg_loss | -56.4698 |
| avg_hold_time_bars | 4.4129 |
| exposure | 0.0899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
