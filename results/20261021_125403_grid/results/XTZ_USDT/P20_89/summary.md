# EMA Hourly Continuation — XTZ/USDT P20_89

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.7314 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9826 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.3441 |
| sortino_ratio | -0.7702 |
| max_drawdown | 0.6127 |
| cagr | -0.2977 |
| net_avg_win | 61.8466 |
| net_avg_loss | -82.0274 |
| avg_hold_time_bars | 17.6407 |
| exposure | 0.4218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
