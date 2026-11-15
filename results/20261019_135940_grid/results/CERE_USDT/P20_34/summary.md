# EMA Hourly Continuation — CERE/USDT P20_34

**Symbol:** CERE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.3035 |
| net_win_rate | 0.2808 |
| gross_profit_factor | 0.7214 |
| gross_win_rate | 0.3506 |
| sharpe_ratio | -16.3541 |
| sortino_ratio | -8.1578 |
| max_drawdown | 1.0000 |
| cagr | -0.9883 |
| net_avg_win | 13.3686 |
| net_avg_loss | -17.1952 |
| avg_hold_time_bars | 4.0215 |
| exposure | 0.2122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
