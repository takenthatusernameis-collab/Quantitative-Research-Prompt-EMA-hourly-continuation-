# EMA Hourly Continuation — SUI/USDT P20_200

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.2079 |
| sortino_ratio | -0.5929 |
| max_drawdown | 0.5428 |
| cagr | -0.2473 |
| net_avg_win | 67.6978 |
| net_avg_loss | -89.1954 |
| avg_hold_time_bars | 38.8493 |
| exposure | 0.6445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
