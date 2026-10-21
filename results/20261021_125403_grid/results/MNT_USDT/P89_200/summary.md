# EMA Hourly Continuation — MNT/USDT P89_200

**Symbol:** MNT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.5345 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.7348 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -2.6692 |
| sortino_ratio | -0.5995 |
| max_drawdown | 0.5195 |
| cagr | -0.2413 |
| net_avg_win | 52.2254 |
| net_avg_loss | -76.7643 |
| avg_hold_time_bars | 18.3920 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
