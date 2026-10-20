# EMA Hourly Continuation — SLP/USDT P55_100

**Symbol:** SLP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.5340 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -5.8479 |
| sortino_ratio | -2.2222 |
| max_drawdown | 0.9325 |
| cagr | -0.6578 |
| net_avg_win | 32.9797 |
| net_avg_loss | -50.9128 |
| avg_hold_time_bars | 5.1980 |
| exposure | 0.1694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
