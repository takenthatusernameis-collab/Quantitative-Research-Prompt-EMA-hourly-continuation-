# EMA Hourly Continuation — UQC/USDT P50_100

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.2561 |
| net_win_rate | 0.2568 |
| gross_profit_factor | 0.3960 |
| gross_win_rate | 0.2793 |
| sharpe_ratio | -6.1820 |
| sortino_ratio | -1.2983 |
| max_drawdown | 0.8088 |
| cagr | -0.4794 |
| net_avg_win | 48.7422 |
| net_avg_loss | -65.7614 |
| avg_hold_time_bars | 37.4054 |
| exposure | 0.3758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
