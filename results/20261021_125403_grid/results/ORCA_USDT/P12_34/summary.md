# EMA Hourly Continuation — ORCA/USDT P12_34

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7549 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0445 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.5327 |
| sortino_ratio | -0.9512 |
| max_drawdown | 0.7135 |
| cagr | -0.3563 |
| net_avg_win | 58.7039 |
| net_avg_loss | -80.9988 |
| avg_hold_time_bars | 7.4753 |
| exposure | 0.2338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
