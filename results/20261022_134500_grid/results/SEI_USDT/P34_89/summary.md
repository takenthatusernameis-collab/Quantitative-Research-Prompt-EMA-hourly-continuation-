# EMA Hourly Continuation — SEI/USDT P34_89

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.5728 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8787 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -5.1580 |
| sortino_ratio | -1.8481 |
| max_drawdown | 0.8984 |
| cagr | -0.5931 |
| net_avg_win | 41.1131 |
| net_avg_loss | -58.5459 |
| avg_hold_time_bars | 8.0415 |
| exposure | 0.2376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
