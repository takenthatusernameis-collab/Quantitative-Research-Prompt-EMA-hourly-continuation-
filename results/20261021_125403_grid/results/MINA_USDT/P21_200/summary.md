# EMA Hourly Continuation — MINA/USDT P21_200

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8668 |
| net_win_rate | 0.5162 |
| gross_profit_factor | 1.0398 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -0.6852 |
| sortino_ratio | -0.1724 |
| max_drawdown | 0.3176 |
| cagr | -0.0792 |
| net_avg_win | 76.5845 |
| net_avg_loss | -94.2824 |
| avg_hold_time_bars | 45.6136 |
| exposure | 0.6386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
