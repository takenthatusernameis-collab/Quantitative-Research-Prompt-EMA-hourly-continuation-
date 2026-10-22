# EMA Hourly Continuation — SQD/USDT P8_100

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.8350 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9686 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.2390 |
| sortino_ratio | -0.4203 |
| max_drawdown | 0.4009 |
| cagr | -0.1791 |
| net_avg_win | 71.3619 |
| net_avg_loss | -83.9114 |
| avg_hold_time_bars | 21.5193 |
| exposure | 0.5513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
