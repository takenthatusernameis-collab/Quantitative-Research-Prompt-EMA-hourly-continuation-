# EMA Hourly Continuation — APT/USDT P89_100

**Symbol:** APT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.2740 |
| net_win_rate | 0.3819 |
| gross_profit_factor | 0.7472 |
| gross_win_rate | 0.4132 |
| sharpe_ratio | -9.1551 |
| sortino_ratio | -3.1778 |
| max_drawdown | 0.9852 |
| cagr | -0.8134 |
| net_avg_win | 16.9040 |
| net_avg_loss | -38.1217 |
| avg_hold_time_bars | 2.0243 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
