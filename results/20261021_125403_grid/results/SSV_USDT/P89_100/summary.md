# EMA Hourly Continuation — SSV/USDT P89_100

**Symbol:** SSV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 135 |
| net_profit_factor | 0.6489 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -1.5152 |
| sortino_ratio | -0.2518 |
| max_drawdown | 0.2637 |
| cagr | -0.1083 |
| net_avg_win | 71.4091 |
| net_avg_loss | -102.1836 |
| avg_hold_time_bars | 4.7852 |
| exposure | 0.0292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
