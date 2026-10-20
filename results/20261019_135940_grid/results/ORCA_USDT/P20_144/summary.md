# EMA Hourly Continuation — ORCA/USDT P20_144

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6045 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8673 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.0266 |
| sortino_ratio | -0.9249 |
| max_drawdown | 0.7076 |
| cagr | -0.3611 |
| net_avg_win | 45.2761 |
| net_avg_loss | -68.3057 |
| avg_hold_time_bars | 26.1088 |
| exposure | 0.5673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
