# EMA Hourly Continuation — NMR/USDT P8_34

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1453 |
| net_profit_factor | 0.5381 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -9.2109 |
| sortino_ratio | -4.9341 |
| max_drawdown | 0.9980 |
| cagr | -0.9129 |
| net_avg_win | 17.9412 |
| net_avg_loss | -26.8374 |
| avg_hold_time_bars | 5.0888 |
| exposure | 0.3361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
