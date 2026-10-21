# EMA Hourly Continuation — DGB/USDT P8_100

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8371 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.2410 |
| sortino_ratio | -0.4001 |
| max_drawdown | 0.3948 |
| cagr | -0.1703 |
| net_avg_win | 75.1610 |
| net_avg_loss | -91.9377 |
| avg_hold_time_bars | 27.5968 |
| exposure | 0.6347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
