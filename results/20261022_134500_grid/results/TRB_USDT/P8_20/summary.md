# EMA Hourly Continuation — TRB/USDT P8_20

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1762 |
| net_profit_factor | 0.3242 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.7113 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -13.6450 |
| sortino_ratio | -8.1141 |
| max_drawdown | 1.0000 |
| cagr | -0.9833 |
| net_avg_win | 6.7476 |
| net_avg_loss | -14.0792 |
| avg_hold_time_bars | 2.9915 |
| exposure | 0.2385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
