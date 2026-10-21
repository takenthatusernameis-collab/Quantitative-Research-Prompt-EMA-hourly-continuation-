# EMA Hourly Continuation — AKT/USDT P26_34

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -1.3254 |
| sortino_ratio | -0.2355 |
| max_drawdown | 0.2605 |
| cagr | -0.1022 |
| net_avg_win | 72.4142 |
| net_avg_loss | -98.7706 |
| avg_hold_time_bars | 6.0714 |
| exposure | 0.0425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
