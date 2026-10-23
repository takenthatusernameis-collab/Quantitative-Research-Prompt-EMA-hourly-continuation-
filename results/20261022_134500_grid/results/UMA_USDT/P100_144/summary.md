# EMA Hourly Continuation — UMA/USDT P100_144

**Symbol:** UMA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.4177 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8425 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -5.3299 |
| sortino_ratio | -1.6844 |
| max_drawdown | 0.8765 |
| cagr | -0.5625 |
| net_avg_win | 27.7565 |
| net_avg_loss | -55.2168 |
| avg_hold_time_bars | 5.1386 |
| exposure | 0.1163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
