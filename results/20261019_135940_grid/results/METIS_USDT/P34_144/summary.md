# EMA Hourly Continuation — METIS/USDT P34_144

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.4991 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.7620 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -4.8370 |
| sortino_ratio | -1.5437 |
| max_drawdown | 0.8493 |
| cagr | -0.5294 |
| net_avg_win | 37.9505 |
| net_avg_loss | -56.5215 |
| avg_hold_time_bars | 17.0880 |
| exposure | 0.4062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
