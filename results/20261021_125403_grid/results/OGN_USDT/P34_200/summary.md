# EMA Hourly Continuation — OGN/USDT P34_200

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7607 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.5208 |
| sortino_ratio | -0.3690 |
| max_drawdown | 0.3938 |
| cagr | -0.1571 |
| net_avg_win | 78.4032 |
| net_avg_loss | -97.5657 |
| avg_hold_time_bars | 40.2466 |
| exposure | 0.5318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
