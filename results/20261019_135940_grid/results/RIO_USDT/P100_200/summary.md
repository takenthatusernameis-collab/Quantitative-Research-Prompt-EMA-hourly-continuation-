# EMA Hourly Continuation — RIO/USDT P100_200

**Symbol:** RIO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.4951 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6881 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -4.6782 |
| sortino_ratio | -1.4221 |
| max_drawdown | 0.8240 |
| cagr | -0.4972 |
| net_avg_win | 41.6069 |
| net_avg_loss | -58.5570 |
| avg_hold_time_bars | 8.2447 |
| exposure | 0.1779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
