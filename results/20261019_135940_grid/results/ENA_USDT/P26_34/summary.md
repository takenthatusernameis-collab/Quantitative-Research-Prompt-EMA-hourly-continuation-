# EMA Hourly Continuation — ENA/USDT P26_34

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.3974 |
| net_win_rate | 0.4241 |
| gross_profit_factor | 0.7781 |
| gross_win_rate | 0.4383 |
| sharpe_ratio | -9.3555 |
| sortino_ratio | -4.3352 |
| max_drawdown | 0.9955 |
| cagr | -0.8824 |
| net_avg_win | 14.5869 |
| net_avg_loss | -27.0340 |
| avg_hold_time_bars | 2.0217 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
