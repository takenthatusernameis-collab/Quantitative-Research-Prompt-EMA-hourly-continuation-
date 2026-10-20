# EMA Hourly Continuation — LUNA/USDT P20_55

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.4641 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.8804 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -9.2401 |
| sortino_ratio | -4.2834 |
| max_drawdown | 0.9955 |
| cagr | -0.8839 |
| net_avg_win | 18.6637 |
| net_avg_loss | -29.7722 |
| avg_hold_time_bars | 4.4190 |
| exposure | 0.2181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
