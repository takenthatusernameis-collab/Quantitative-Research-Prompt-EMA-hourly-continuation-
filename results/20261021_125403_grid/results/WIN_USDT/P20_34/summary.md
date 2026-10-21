# EMA Hourly Continuation — WIN/USDT P20_34

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.5857 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.9355 |
| sortino_ratio | -0.7258 |
| max_drawdown | 0.5726 |
| cagr | -0.2829 |
| net_avg_win | 56.3755 |
| net_avg_loss | -89.9177 |
| avg_hold_time_bars | 5.9490 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
