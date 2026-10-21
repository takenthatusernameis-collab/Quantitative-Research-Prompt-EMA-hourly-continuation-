# EMA Hourly Continuation — SSV/USDT P8_200

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.8236 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -0.7732 |
| sortino_ratio | -0.1542 |
| max_drawdown | 0.2592 |
| cagr | -0.0695 |
| net_avg_win | 80.8573 |
| net_avg_loss | -94.2480 |
| avg_hold_time_bars | 97.5765 |
| exposure | 0.8654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
