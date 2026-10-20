# EMA Hourly Continuation — ID/USDT P34_89

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.5348 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -4.3439 |
| sortino_ratio | -1.5833 |
| max_drawdown | 0.8437 |
| cagr | -0.5196 |
| net_avg_win | 31.6549 |
| net_avg_loss | -51.3102 |
| avg_hold_time_bars | 7.8012 |
| exposure | 0.2327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
