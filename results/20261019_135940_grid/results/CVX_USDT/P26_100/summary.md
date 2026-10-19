# EMA Hourly Continuation — CVX/USDT P26_100

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.5881 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8662 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -4.2265 |
| sortino_ratio | -1.5155 |
| max_drawdown | 0.8450 |
| cagr | -0.5204 |
| net_avg_win | 39.5534 |
| net_avg_loss | -57.7527 |
| avg_hold_time_bars | 10.8176 |
| exposure | 0.3235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
