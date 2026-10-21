# EMA Hourly Continuation — GRT/USDT P12_100

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8459 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0307 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.1682 |
| sortino_ratio | -0.3454 |
| max_drawdown | 0.4650 |
| cagr | -0.1490 |
| net_avg_win | 84.5777 |
| net_avg_loss | -102.8296 |
| avg_hold_time_bars | 30.1659 |
| exposure | 0.5842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
