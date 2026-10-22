# EMA Hourly Continuation — METIS/USDT P20_144

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7220 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -2.1066 |
| sortino_ratio | -0.5980 |
| max_drawdown | 0.5137 |
| cagr | -0.2408 |
| net_avg_win | 70.0998 |
| net_avg_loss | -83.5440 |
| avg_hold_time_bars | 28.1675 |
| exposure | 0.5121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
