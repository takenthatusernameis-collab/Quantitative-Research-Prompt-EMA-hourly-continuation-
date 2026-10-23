# EMA Hourly Continuation — QI/USDT P21_50

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.4790 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8576 |
| gross_win_rate | 0.4616 |
| sharpe_ratio | -7.1421 |
| sortino_ratio | -3.0261 |
| max_drawdown | 0.9767 |
| cagr | -0.7723 |
| net_avg_win | 22.2120 |
| net_avg_loss | -36.8786 |
| avg_hold_time_bars | 5.1064 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
