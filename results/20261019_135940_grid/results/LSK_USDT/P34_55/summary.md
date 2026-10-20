# EMA Hourly Continuation — LSK/USDT P34_55

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.4684 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.9863 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -6.8172 |
| sortino_ratio | -2.6489 |
| max_drawdown | 0.9631 |
| cagr | -0.7285 |
| net_avg_win | 24.7912 |
| net_avg_loss | -44.5819 |
| avg_hold_time_bars | 4.1551 |
| exposure | 0.1413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
