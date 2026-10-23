# EMA Hourly Continuation — VR/USDT P21_26

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1273 |
| net_profit_factor | 0.2054 |
| net_win_rate | 0.2278 |
| gross_profit_factor | 0.5210 |
| gross_win_rate | 0.2710 |
| sharpe_ratio | -20.8568 |
| sortino_ratio | -11.6726 |
| max_drawdown | 1.0000 |
| cagr | -0.9989 |
| net_avg_win | 8.9151 |
| net_avg_loss | -12.8030 |
| avg_hold_time_bars | 2.1493 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
