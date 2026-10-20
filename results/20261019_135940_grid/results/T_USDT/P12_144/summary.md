# EMA Hourly Continuation — T/USDT P12_144

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7497 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.1653 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -1.9860 |
| sortino_ratio | -0.5516 |
| max_drawdown | 0.5486 |
| cagr | -0.2303 |
| net_avg_win | 74.6060 |
| net_avg_loss | -100.0364 |
| avg_hold_time_bars | 38.9897 |
| exposure | 0.6828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
