# EMA Hourly Continuation — ARKM/USDT P20_144

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7837 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -1.4080 |
| sortino_ratio | -0.3799 |
| max_drawdown | 0.3681 |
| cagr | -0.1612 |
| net_avg_win | 75.1916 |
| net_avg_loss | -88.2493 |
| avg_hold_time_bars | 33.3370 |
| exposure | 0.5440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
