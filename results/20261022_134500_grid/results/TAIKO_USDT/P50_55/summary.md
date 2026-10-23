# EMA Hourly Continuation — TAIKO/USDT P50_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.2182 |
| net_win_rate | 0.3235 |
| gross_profit_factor | 0.6469 |
| gross_win_rate | 0.3896 |
| sharpe_ratio | -12.7297 |
| sortino_ratio | -5.1789 |
| max_drawdown | 0.9989 |
| cagr | -0.9416 |
| net_avg_win | 12.1196 |
| net_avg_loss | -26.5609 |
| avg_hold_time_bars | 2.0450 |
| exposure | 0.0698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
