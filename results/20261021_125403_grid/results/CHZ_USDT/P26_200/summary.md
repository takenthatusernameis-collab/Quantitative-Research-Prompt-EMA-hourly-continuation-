# EMA Hourly Continuation — CHZ/USDT P26_200

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.9457 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1462 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.2532 |
| sortino_ratio | -0.0612 |
| max_drawdown | 0.2915 |
| cagr | -0.0320 |
| net_avg_win | 90.4039 |
| net_avg_loss | -111.0373 |
| avg_hold_time_bars | 47.4875 |
| exposure | 0.6065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
