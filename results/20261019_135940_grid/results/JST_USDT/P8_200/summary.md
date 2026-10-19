# EMA Hourly Continuation — JST/USDT P8_200

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6388 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0562 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -2.3419 |
| sortino_ratio | -0.6217 |
| max_drawdown | 0.5550 |
| cagr | -0.2603 |
| net_avg_win | 52.0493 |
| net_avg_loss | -81.0294 |
| avg_hold_time_bars | 47.2645 |
| exposure | 0.7764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
