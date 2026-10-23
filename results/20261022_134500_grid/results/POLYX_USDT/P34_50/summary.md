# EMA Hourly Continuation — POLYX/USDT P34_50

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 876 |
| net_profit_factor | 0.4259 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -8.0714 |
| sortino_ratio | -3.3739 |
| max_drawdown | 0.9865 |
| cagr | -0.8160 |
| net_avg_win | 18.8019 |
| net_avg_loss | -35.2598 |
| avg_hold_time_bars | 3.2500 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
