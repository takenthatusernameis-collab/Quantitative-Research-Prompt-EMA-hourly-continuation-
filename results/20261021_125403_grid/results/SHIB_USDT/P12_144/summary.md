# EMA Hourly Continuation — SHIB/USDT P12_144

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.9362 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1669 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.3711 |
| sortino_ratio | -0.1042 |
| max_drawdown | 0.2668 |
| cagr | -0.0514 |
| net_avg_win | 89.7931 |
| net_avg_loss | -111.8932 |
| avg_hold_time_bars | 36.7692 |
| exposure | 0.6301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
