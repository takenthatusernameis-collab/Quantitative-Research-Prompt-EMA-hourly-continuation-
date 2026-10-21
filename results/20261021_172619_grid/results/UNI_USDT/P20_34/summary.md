# EMA Hourly Continuation — UNI/USDT P20_34

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6944 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.7466 |
| sortino_ratio | -0.4071 |
| max_drawdown | 0.4127 |
| cagr | -0.1694 |
| net_avg_win | 65.1094 |
| net_avg_loss | -90.9645 |
| avg_hold_time_bars | 5.0871 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
