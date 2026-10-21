# EMA Hourly Continuation — AR/USDT P12_50

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7972 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.9348 |
| sortino_ratio | -0.6895 |
| max_drawdown | 0.5773 |
| cagr | -0.2732 |
| net_avg_win | 70.5892 |
| net_avg_loss | -86.5715 |
| avg_hold_time_bars | 12.5588 |
| exposure | 0.3545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
