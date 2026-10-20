# EMA Hourly Continuation — SLP/USDT P50_89

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.5500 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.9623 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -6.3865 |
| sortino_ratio | -2.5000 |
| max_drawdown | 0.9549 |
| cagr | -0.7065 |
| net_avg_win | 33.7924 |
| net_avg_loss | -50.4714 |
| avg_hold_time_bars | 4.6784 |
| exposure | 0.1627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
