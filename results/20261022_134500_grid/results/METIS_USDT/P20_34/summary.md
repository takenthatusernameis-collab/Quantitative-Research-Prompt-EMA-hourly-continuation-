# EMA Hourly Continuation — METIS/USDT P20_34

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.3693 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4278 |
| sharpe_ratio | -10.8733 |
| sortino_ratio | -5.2908 |
| max_drawdown | 0.9988 |
| cagr | -0.9312 |
| net_avg_win | 12.2590 |
| net_avg_loss | -22.5899 |
| avg_hold_time_bars | 2.7827 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
