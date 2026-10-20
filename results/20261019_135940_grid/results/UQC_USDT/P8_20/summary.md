# EMA Hourly Continuation — UQC/USDT P8_20

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.1177 |
| net_win_rate | 0.1907 |
| gross_profit_factor | 0.3675 |
| gross_win_rate | 0.2560 |
| sharpe_ratio | -16.6410 |
| sortino_ratio | -7.3857 |
| max_drawdown | 1.0000 |
| cagr | -0.9839 |
| net_avg_win | 8.7803 |
| net_avg_loss | -17.5726 |
| avg_hold_time_bars | 10.6211 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
