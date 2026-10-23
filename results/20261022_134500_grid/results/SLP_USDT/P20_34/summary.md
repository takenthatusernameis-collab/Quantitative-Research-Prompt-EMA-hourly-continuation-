# EMA Hourly Continuation — SLP/USDT P20_34

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.3970 |
| net_win_rate | 0.3901 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4179 |
| sharpe_ratio | -12.4991 |
| sortino_ratio | -6.5103 |
| max_drawdown | 0.9998 |
| cagr | -0.9634 |
| net_avg_win | 12.6555 |
| net_avg_loss | -20.3916 |
| avg_hold_time_bars | 2.6594 |
| exposure | 0.1611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
