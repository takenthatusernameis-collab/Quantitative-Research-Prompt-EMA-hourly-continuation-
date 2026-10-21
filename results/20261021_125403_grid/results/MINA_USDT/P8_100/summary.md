# EMA Hourly Continuation — MINA/USDT P8_100

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.2223 |
| sortino_ratio | -0.4002 |
| max_drawdown | 0.4546 |
| cagr | -0.1710 |
| net_avg_win | 69.7530 |
| net_avg_loss | -87.1473 |
| avg_hold_time_bars | 27.8966 |
| exposure | 0.6619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
