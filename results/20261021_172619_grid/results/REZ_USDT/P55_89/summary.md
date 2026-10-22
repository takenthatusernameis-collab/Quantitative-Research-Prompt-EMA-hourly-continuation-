# EMA Hourly Continuation — REZ/USDT P55_89

**Symbol:** REZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8906 |
| net_win_rate | 0.5378 |
| gross_profit_factor | 1.1458 |
| gross_win_rate | 0.5378 |
| sharpe_ratio | -0.6252 |
| sortino_ratio | -0.1720 |
| max_drawdown | 0.2640 |
| cagr | -0.0794 |
| net_avg_win | 78.4601 |
| net_avg_loss | -102.5168 |
| avg_hold_time_bars | 7.0196 |
| exposure | 0.1156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
