# EMA Hourly Continuation — POKT/USDT P34_100

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.5800 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -6.0456 |
| sortino_ratio | -2.3367 |
| max_drawdown | 0.9449 |
| cagr | -0.6788 |
| net_avg_win | 39.7004 |
| net_avg_loss | -51.7325 |
| avg_hold_time_bars | 9.1890 |
| exposure | 0.3169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
