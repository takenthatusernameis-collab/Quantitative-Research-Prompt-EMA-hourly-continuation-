# EMA Hourly Continuation — RSR/USDT P26_89

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8675 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0637 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.9614 |
| sortino_ratio | -0.2975 |
| max_drawdown | 0.3440 |
| cagr | -0.1308 |
| net_avg_win | 81.2587 |
| net_avg_loss | -99.5030 |
| avg_hold_time_bars | 13.1918 |
| exposure | 0.2782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
