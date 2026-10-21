# EMA Hourly Continuation — RLC/USDT P8_200

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0732 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -1.1224 |
| sortino_ratio | -0.2828 |
| max_drawdown | 0.4053 |
| cagr | -0.1242 |
| net_avg_win | 77.7426 |
| net_avg_loss | -100.4701 |
| avg_hold_time_bars | 58.8910 |
| exposure | 0.8352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
