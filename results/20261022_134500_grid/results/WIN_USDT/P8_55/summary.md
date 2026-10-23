# EMA Hourly Continuation — WIN/USDT P8_55

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.4368 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -8.6267 |
| sortino_ratio | -3.8725 |
| max_drawdown | 0.9934 |
| cagr | -0.8631 |
| net_avg_win | 17.4675 |
| net_avg_loss | -29.8398 |
| avg_hold_time_bars | 10.5601 |
| exposure | 0.4954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
