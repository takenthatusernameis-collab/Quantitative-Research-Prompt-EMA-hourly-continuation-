# EMA Hourly Continuation — ZRO/USDT P20_200

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8466 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -0.8298 |
| sortino_ratio | -0.2028 |
| max_drawdown | 0.2441 |
| cagr | -0.0912 |
| net_avg_win | 82.3180 |
| net_avg_loss | -94.4203 |
| avg_hold_time_bars | 47.4485 |
| exposure | 0.6317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
