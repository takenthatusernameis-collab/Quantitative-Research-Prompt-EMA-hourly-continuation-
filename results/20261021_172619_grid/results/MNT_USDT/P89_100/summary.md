# EMA Hourly Continuation — MNT/USDT P89_100

**Symbol:** MNT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.5003 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8164 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -2.2207 |
| sortino_ratio | -0.3470 |
| max_drawdown | 0.3895 |
| cagr | -0.1480 |
| net_avg_win | 61.3977 |
| net_avg_loss | -103.5524 |
| avg_hold_time_bars | 6.2373 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
