# EMA Hourly Continuation — THETA/USDT P50_55

**Symbol:** THETA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.2666 |
| net_win_rate | 0.3807 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -11.5372 |
| sortino_ratio | -4.7620 |
| max_drawdown | 0.9985 |
| cagr | -0.9243 |
| net_avg_win | 11.7849 |
| net_avg_loss | -27.1745 |
| avg_hold_time_bars | 1.8653 |
| exposure | 0.0686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
