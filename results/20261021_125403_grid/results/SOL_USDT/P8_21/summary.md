# EMA Hourly Continuation — SOL/USDT P8_21

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.5365 |
| gross_profit_factor | 1.1403 |
| gross_win_rate | 0.5365 |
| sharpe_ratio | -1.5653 |
| sortino_ratio | -0.4892 |
| max_drawdown | 0.4374 |
| cagr | -0.2002 |
| net_avg_win | 64.2968 |
| net_avg_loss | -94.2924 |
| avg_hold_time_bars | 5.8970 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
