# EMA Hourly Continuation — ARB/USDT P144_200

**Symbol:** ARB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.4768 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8965 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -4.3057 |
| sortino_ratio | -1.1394 |
| max_drawdown | 0.7551 |
| cagr | -0.4272 |
| net_avg_win | 42.9016 |
| net_avg_loss | -75.7731 |
| avg_hold_time_bars | 4.4229 |
| exposure | 0.0704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
