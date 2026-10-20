# EMA Hourly Continuation — WIN/USDT P12_50

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.3874 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -9.8671 |
| sortino_ratio | -4.5479 |
| max_drawdown | 0.9973 |
| cagr | -0.9039 |
| net_avg_win | 14.2338 |
| net_avg_loss | -25.9199 |
| avg_hold_time_bars | 6.9795 |
| exposure | 0.3398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
