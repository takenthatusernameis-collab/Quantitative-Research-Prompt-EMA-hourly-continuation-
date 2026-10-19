# EMA Hourly Continuation — UNI/USDT P34_50

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.2952 |
| net_win_rate | 0.3994 |
| gross_profit_factor | 0.6658 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -10.4494 |
| sortino_ratio | -4.5911 |
| max_drawdown | 0.9974 |
| cagr | -0.9055 |
| net_avg_win | 10.9645 |
| net_avg_loss | -24.6958 |
| avg_hold_time_bars | 2.5356 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
