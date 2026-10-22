# EMA Hourly Continuation — RSR/USDT P12_55

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1037 |
| net_profit_factor | 0.6283 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -5.3669 |
| sortino_ratio | -2.4317 |
| max_drawdown | 0.9479 |
| cagr | -0.6879 |
| net_avg_win | 32.9746 |
| net_avg_loss | -46.1150 |
| avg_hold_time_bars | 7.6924 |
| exposure | 0.3626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
