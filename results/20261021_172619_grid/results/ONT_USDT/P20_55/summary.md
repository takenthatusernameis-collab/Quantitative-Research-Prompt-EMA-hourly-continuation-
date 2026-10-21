# EMA Hourly Continuation — ONT/USDT P20_55

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1287 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -1.3728 |
| sortino_ratio | -0.4520 |
| max_drawdown | 0.4834 |
| cagr | -0.1887 |
| net_avg_win | 73.3593 |
| net_avg_loss | -99.2700 |
| avg_hold_time_bars | 8.1224 |
| exposure | 0.1922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
