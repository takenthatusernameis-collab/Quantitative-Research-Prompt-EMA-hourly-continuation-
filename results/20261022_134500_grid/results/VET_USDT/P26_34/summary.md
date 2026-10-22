# EMA Hourly Continuation — VET/USDT P26_34

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.2032 |
| net_win_rate | 0.3683 |
| gross_profit_factor | 0.6488 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -13.0583 |
| sortino_ratio | -6.0791 |
| max_drawdown | 0.9997 |
| cagr | -0.9612 |
| net_avg_win | 6.7809 |
| net_avg_loss | -19.4524 |
| avg_hold_time_bars | 2.0803 |
| exposure | 0.0965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
