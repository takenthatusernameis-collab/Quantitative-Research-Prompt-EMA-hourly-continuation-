# EMA Hourly Continuation — ALT/USDT P34_50

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 815 |
| net_profit_factor | 0.4197 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8084 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -7.3402 |
| sortino_ratio | -2.9571 |
| max_drawdown | 0.9748 |
| cagr | -0.7674 |
| net_avg_win | 19.7390 |
| net_avg_loss | -36.6596 |
| avg_hold_time_bars | 4.0479 |
| exposure | 0.1500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
