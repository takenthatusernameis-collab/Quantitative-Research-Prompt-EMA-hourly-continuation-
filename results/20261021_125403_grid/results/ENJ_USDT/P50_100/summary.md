# EMA Hourly Continuation — ENJ/USDT P50_100

**Symbol:** ENJ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7460 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.7763 |
| sortino_ratio | -0.4875 |
| max_drawdown | 0.4557 |
| cagr | -0.2008 |
| net_avg_win | 69.3025 |
| net_avg_loss | -91.8940 |
| avg_hold_time_bars | 9.2609 |
| exposure | 0.1542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
