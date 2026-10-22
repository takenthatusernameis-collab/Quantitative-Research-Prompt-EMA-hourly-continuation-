# EMA Hourly Continuation — CVX/USDT P8_50

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.5424 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8286 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -6.0528 |
| sortino_ratio | -2.8177 |
| max_drawdown | 0.9675 |
| cagr | -0.7429 |
| net_avg_win | 22.9725 |
| net_avg_loss | -35.0468 |
| avg_hold_time_bars | 9.4410 |
| exposure | 0.4729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
