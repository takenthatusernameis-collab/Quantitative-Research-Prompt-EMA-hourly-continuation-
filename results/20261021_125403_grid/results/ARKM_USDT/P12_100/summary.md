# EMA Hourly Continuation — ARKM/USDT P12_100

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8181 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.3623 |
| sortino_ratio | -0.4127 |
| max_drawdown | 0.4224 |
| cagr | -0.1750 |
| net_avg_win | 77.6083 |
| net_avg_loss | -91.9633 |
| avg_hold_time_bars | 27.7317 |
| exposure | 0.5685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
