# EMA Hourly Continuation — KCS/USDT P50_100

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.2089 |
| net_win_rate | 0.3740 |
| gross_profit_factor | 0.6991 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -10.2160 |
| sortino_ratio | -3.8007 |
| max_drawdown | 0.9938 |
| cagr | -0.8661 |
| net_avg_win | 10.7091 |
| net_avg_loss | -30.6331 |
| avg_hold_time_bars | 6.3908 |
| exposure | 0.1903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
