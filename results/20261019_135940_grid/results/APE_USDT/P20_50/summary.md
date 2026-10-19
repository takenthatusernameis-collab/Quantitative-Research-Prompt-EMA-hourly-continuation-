# EMA Hourly Continuation — APE/USDT P20_50

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5002 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -7.0117 |
| sortino_ratio | -3.1650 |
| max_drawdown | 0.9806 |
| cagr | -0.7876 |
| net_avg_win | 20.5532 |
| net_avg_loss | -35.4422 |
| avg_hold_time_bars | 4.0194 |
| exposure | 0.1882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
