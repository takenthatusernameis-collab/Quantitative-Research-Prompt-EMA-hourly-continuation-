# EMA Hourly Continuation — EUL/USDT P55_200

**Symbol:** EUL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5200 |
| net_win_rate | 0.4160 |
| gross_profit_factor | 0.7340 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -3.9974 |
| sortino_ratio | -1.0989 |
| max_drawdown | 0.7409 |
| cagr | -0.4097 |
| net_avg_win | 49.3737 |
| net_avg_loss | -67.6441 |
| avg_hold_time_bars | 16.5323 |
| exposure | 0.2908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
