# EMA Hourly Continuation — NOT/USDT P12_89

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9168 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.3689 |
| sortino_ratio | -1.6438 |
| max_drawdown | 0.8606 |
| cagr | -0.5481 |
| net_avg_win | 41.4806 |
| net_avg_loss | -59.8142 |
| avg_hold_time_bars | 16.9094 |
| exposure | 0.5520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
