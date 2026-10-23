# EMA Hourly Continuation — RPL/USDT P8_20

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1432 |
| net_profit_factor | 0.4843 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 1.0392 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -8.3119 |
| sortino_ratio | -4.4128 |
| max_drawdown | 0.9959 |
| cagr | -0.8865 |
| net_avg_win | 13.9797 |
| net_avg_loss | -25.3095 |
| avg_hold_time_bars | 3.9623 |
| exposure | 0.2568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
