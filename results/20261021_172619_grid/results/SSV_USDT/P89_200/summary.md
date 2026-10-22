# EMA Hourly Continuation — SSV/USDT P89_200

**Symbol:** SSV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8606 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.1383 |
| sortino_ratio | -0.5363 |
| max_drawdown | 0.4894 |
| cagr | -0.2185 |
| net_avg_win | 67.3155 |
| net_avg_loss | -86.1809 |
| avg_hold_time_bars | 13.2596 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
