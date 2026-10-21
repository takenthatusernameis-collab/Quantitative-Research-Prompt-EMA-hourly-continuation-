# EMA Hourly Continuation — HNT/USDT P12_200

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.8750 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0126 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -0.6511 |
| sortino_ratio | -0.1611 |
| max_drawdown | 0.2207 |
| cagr | -0.0744 |
| net_avg_win | 81.7907 |
| net_avg_loss | -96.0143 |
| avg_hold_time_bars | 53.4396 |
| exposure | 0.7239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
