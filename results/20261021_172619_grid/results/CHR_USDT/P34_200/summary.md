# EMA Hourly Continuation — CHR/USDT P34_200

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.9367 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.1083 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -0.3017 |
| sortino_ratio | -0.0744 |
| max_drawdown | 0.2810 |
| cagr | -0.0377 |
| net_avg_win | 88.2360 |
| net_avg_loss | -105.0450 |
| avg_hold_time_bars | 41.1633 |
| exposure | 0.5476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
