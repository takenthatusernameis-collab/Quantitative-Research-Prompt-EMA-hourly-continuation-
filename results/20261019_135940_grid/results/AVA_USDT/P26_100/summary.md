# EMA Hourly Continuation — AVA/USDT P26_100

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5520 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -4.2891 |
| sortino_ratio | -1.5568 |
| max_drawdown | 0.8679 |
| cagr | -0.5356 |
| net_avg_win | 32.3907 |
| net_avg_loss | -54.9577 |
| avg_hold_time_bars | 11.1057 |
| exposure | 0.3392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
