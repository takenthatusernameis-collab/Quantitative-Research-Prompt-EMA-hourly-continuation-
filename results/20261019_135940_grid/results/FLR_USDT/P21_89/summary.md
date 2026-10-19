# EMA Hourly Continuation — FLR/USDT P21_89

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.4995 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8778 |
| gross_win_rate | 0.4452 |
| sharpe_ratio | -7.2048 |
| sortino_ratio | -2.9648 |
| max_drawdown | 0.9761 |
| cagr | -0.7732 |
| net_avg_win | 26.0439 |
| net_avg_loss | -39.5529 |
| avg_hold_time_bars | 9.1315 |
| exposure | 0.3599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
