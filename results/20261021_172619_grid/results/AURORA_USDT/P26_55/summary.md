# EMA Hourly Continuation — AURORA/USDT P26_55

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.7641 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -4.4548 |
| sortino_ratio | -1.2957 |
| max_drawdown | 0.7863 |
| cagr | -0.4540 |
| net_avg_win | 46.4409 |
| net_avg_loss | -67.5575 |
| avg_hold_time_bars | 9.0385 |
| exposure | 0.1709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
