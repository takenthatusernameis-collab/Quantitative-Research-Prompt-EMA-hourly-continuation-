# EMA Hourly Continuation — KSM/USDT P50_144

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7502 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9788 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.7597 |
| sortino_ratio | -0.4817 |
| max_drawdown | 0.4647 |
| cagr | -0.1990 |
| net_avg_win | 70.8619 |
| net_avg_loss | -92.4183 |
| avg_hold_time_bars | 15.6421 |
| exposure | 0.2602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
