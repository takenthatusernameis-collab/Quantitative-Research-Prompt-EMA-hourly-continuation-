# EMA Hourly Continuation — SEI/USDT P21_89

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -4.1686 |
| sortino_ratio | -1.5274 |
| max_drawdown | 0.8516 |
| cagr | -0.5235 |
| net_avg_win | 49.3581 |
| net_avg_loss | -67.9871 |
| avg_hold_time_bars | 12.6912 |
| exposure | 0.3923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
