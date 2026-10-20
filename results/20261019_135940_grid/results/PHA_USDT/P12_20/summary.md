# EMA Hourly Continuation — PHA/USDT P12_20

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1468 |
| net_profit_factor | 0.3445 |
| net_win_rate | 0.4285 |
| gross_profit_factor | 0.8540 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -11.3133 |
| sortino_ratio | -6.1073 |
| max_drawdown | 0.9996 |
| cagr | -0.9558 |
| net_avg_win | 8.3526 |
| net_avg_loss | -18.1762 |
| avg_hold_time_bars | 2.3488 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
