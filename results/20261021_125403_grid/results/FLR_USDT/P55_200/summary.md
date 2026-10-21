# EMA Hourly Continuation — FLR/USDT P55_200

**Symbol:** FLR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.8084 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0423 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.3071 |
| sortino_ratio | -0.3609 |
| max_drawdown | 0.3945 |
| cagr | -0.1542 |
| net_avg_win | 76.6561 |
| net_avg_loss | -99.0135 |
| avg_hold_time_bars | 18.2541 |
| exposure | 0.3070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
