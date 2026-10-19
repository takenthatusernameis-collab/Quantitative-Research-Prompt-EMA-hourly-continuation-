# EMA Hourly Continuation — TRX/USDT P21_100

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.3273 |
| net_win_rate | 0.4113 |
| gross_profit_factor | 0.8969 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -8.5089 |
| sortino_ratio | -2.9729 |
| max_drawdown | 0.9812 |
| cagr | -0.7938 |
| net_avg_win | 19.2456 |
| net_avg_loss | -41.0793 |
| avg_hold_time_bars | 14.0829 |
| exposure | 0.3860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
