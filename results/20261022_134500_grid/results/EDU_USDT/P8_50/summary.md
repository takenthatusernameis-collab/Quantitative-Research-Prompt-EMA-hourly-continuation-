# EMA Hourly Continuation — EDU/USDT P8_50

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.5710 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8601 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -5.5743 |
| sortino_ratio | -2.6065 |
| max_drawdown | 0.9563 |
| cagr | -0.7094 |
| net_avg_win | 24.9466 |
| net_avg_loss | -37.6351 |
| avg_hold_time_bars | 9.6198 |
| exposure | 0.4797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
