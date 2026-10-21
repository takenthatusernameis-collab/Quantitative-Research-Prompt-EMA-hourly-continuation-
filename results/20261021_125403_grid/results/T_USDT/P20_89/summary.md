# EMA Hourly Continuation — T/USDT P20_89

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7452 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0320 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -2.3863 |
| sortino_ratio | -0.7766 |
| max_drawdown | 0.6395 |
| cagr | -0.2997 |
| net_avg_win | 66.9622 |
| net_avg_loss | -89.5085 |
| avg_hold_time_bars | 15.6763 |
| exposure | 0.3682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
