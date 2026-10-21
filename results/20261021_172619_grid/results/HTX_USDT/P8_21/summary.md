# EMA Hourly Continuation — HTX/USDT P8_21

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.3941 |
| net_win_rate | 0.3591 |
| gross_profit_factor | 0.7130 |
| gross_win_rate | 0.3650 |
| sharpe_ratio | -9.4137 |
| sortino_ratio | -3.5630 |
| max_drawdown | 0.9865 |
| cagr | -0.8178 |
| net_avg_win | 26.5112 |
| net_avg_loss | -37.6837 |
| avg_hold_time_bars | 6.1113 |
| exposure | 0.1864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
