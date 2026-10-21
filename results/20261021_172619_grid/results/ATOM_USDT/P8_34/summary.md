# EMA Hourly Continuation — ATOM/USDT P8_34

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.8129 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.1106 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -1.9062 |
| sortino_ratio | -0.7251 |
| max_drawdown | 0.6127 |
| cagr | -0.2824 |
| net_avg_win | 67.8484 |
| net_avg_loss | -90.4648 |
| avg_hold_time_bars | 9.6810 |
| exposure | 0.3063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
