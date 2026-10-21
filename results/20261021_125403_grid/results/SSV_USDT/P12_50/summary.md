# EMA Hourly Continuation — SSV/USDT P12_50

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.7231 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.2839 |
| sortino_ratio | -1.2304 |
| max_drawdown | 0.7741 |
| cagr | -0.4328 |
| net_avg_win | 61.8811 |
| net_avg_loss | -72.8697 |
| avg_hold_time_bars | 10.5014 |
| exposure | 0.3317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
