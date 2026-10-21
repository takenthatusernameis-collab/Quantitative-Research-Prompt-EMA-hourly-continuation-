# EMA Hourly Continuation — ONT/USDT P8_89

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.7487 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -2.1713 |
| sortino_ratio | -0.7298 |
| max_drawdown | 0.5891 |
| cagr | -0.2858 |
| net_avg_win | 63.6249 |
| net_avg_loss | -78.2600 |
| avg_hold_time_bars | 23.6190 |
| exposure | 0.5974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
