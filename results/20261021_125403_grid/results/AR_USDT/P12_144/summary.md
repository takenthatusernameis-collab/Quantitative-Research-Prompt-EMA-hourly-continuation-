# EMA Hourly Continuation — AR/USDT P12_144

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.9648 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0923 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -0.1514 |
| sortino_ratio | -0.0377 |
| max_drawdown | 0.1939 |
| cagr | -0.0222 |
| net_avg_win | 96.3275 |
| net_avg_loss | -109.6822 |
| avg_hold_time_bars | 55.1711 |
| exposure | 0.7473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
