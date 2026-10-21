# EMA Hourly Continuation — ZEN/USDT P50_200

**Symbol:** ZEN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7376 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9057 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -1.6923 |
| sortino_ratio | -0.4464 |
| max_drawdown | 0.4328 |
| cagr | -0.1869 |
| net_avg_win | 69.4532 |
| net_avg_loss | -86.2720 |
| avg_hold_time_bars | 24.5190 |
| exposure | 0.3823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
