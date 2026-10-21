# EMA Hourly Continuation — DGB/USDT P20_200

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7997 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.3682 |
| sortino_ratio | -0.3675 |
| max_drawdown | 0.4132 |
| cagr | -0.1570 |
| net_avg_win | 80.5323 |
| net_avg_loss | -95.7185 |
| avg_hold_time_bars | 38.5380 |
| exposure | 0.6219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
