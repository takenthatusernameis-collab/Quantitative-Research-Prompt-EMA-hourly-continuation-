# EMA Hourly Continuation — YGG/USDT P20_21

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.5956 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8533 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -2.2762 |
| sortino_ratio | -0.4403 |
| max_drawdown | 0.4156 |
| cagr | -0.1829 |
| net_avg_win | 70.0185 |
| net_avg_loss | -98.7477 |
| avg_hold_time_bars | 3.7283 |
| exposure | 0.0310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
