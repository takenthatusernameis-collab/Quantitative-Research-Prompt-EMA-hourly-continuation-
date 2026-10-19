# EMA Hourly Continuation — BCH/USDT P26_50

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.3797 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -9.0030 |
| sortino_ratio | -3.9482 |
| max_drawdown | 0.9934 |
| cagr | -0.8631 |
| net_avg_win | 14.1039 |
| net_avg_loss | -30.6137 |
| avg_hold_time_bars | 3.7820 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
