# EMA Hourly Continuation — ICP/USDT P8_200

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7240 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0473 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -2.0179 |
| sortino_ratio | -0.5456 |
| max_drawdown | 0.5132 |
| cagr | -0.2324 |
| net_avg_win | 67.3379 |
| net_avg_loss | -96.0622 |
| avg_hold_time_bars | 47.5780 |
| exposure | 0.8045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
