# EMA Hourly Continuation — WIN/USDT P26_200

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -2.7722 |
| sortino_ratio | -0.7321 |
| max_drawdown | 0.6221 |
| cagr | -0.2989 |
| net_avg_win | 49.0902 |
| net_avg_loss | -78.8114 |
| avg_hold_time_bars | 33.5565 |
| exposure | 0.5400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
