# EMA Hourly Continuation — NMR/USDT P21_50

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.6709 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -3.4893 |
| sortino_ratio | -1.1956 |
| max_drawdown | 0.7552 |
| cagr | -0.4225 |
| net_avg_win | 56.2890 |
| net_avg_loss | -74.2991 |
| avg_hold_time_bars | 7.1456 |
| exposure | 0.1874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
