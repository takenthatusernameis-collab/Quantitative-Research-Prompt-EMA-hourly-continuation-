# EMA Hourly Continuation — WAVES/USDT P12_100

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 836 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -6.2619 |
| sortino_ratio | -2.5372 |
| max_drawdown | 0.9593 |
| cagr | -0.7159 |
| net_avg_win | 30.6088 |
| net_avg_loss | -45.1770 |
| avg_hold_time_bars | 14.3122 |
| exposure | 0.5439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
