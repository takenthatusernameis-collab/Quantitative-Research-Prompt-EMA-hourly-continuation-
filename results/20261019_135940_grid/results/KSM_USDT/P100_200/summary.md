# EMA Hourly Continuation — KSM/USDT P100_200

**Symbol:** KSM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5865 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9743 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -3.3168 |
| sortino_ratio | -0.9381 |
| max_drawdown | 0.7037 |
| cagr | -0.3634 |
| net_avg_win | 49.5998 |
| net_avg_loss | -78.8727 |
| avg_hold_time_bars | 8.8557 |
| exposure | 0.1618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
