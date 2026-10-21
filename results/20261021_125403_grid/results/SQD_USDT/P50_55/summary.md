# EMA Hourly Continuation — SQD/USDT P50_55

**Symbol:** SQD/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 119 |
| net_profit_factor | 0.7438 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9505 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.0221 |
| sortino_ratio | -0.1621 |
| max_drawdown | 0.1948 |
| cagr | -0.0713 |
| net_avg_win | 82.2850 |
| net_avg_loss | -105.1817 |
| avg_hold_time_bars | 6.3950 |
| exposure | 0.0358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
