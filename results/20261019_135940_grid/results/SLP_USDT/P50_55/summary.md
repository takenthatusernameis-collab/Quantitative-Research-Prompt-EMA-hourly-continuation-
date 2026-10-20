# EMA Hourly Continuation — SLP/USDT P50_55

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.2628 |
| net_win_rate | 0.3474 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4171 |
| sharpe_ratio | -13.3105 |
| sortino_ratio | -6.0216 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 10.8297 |
| net_avg_loss | -21.9417 |
| avg_hold_time_bars | 1.9567 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
