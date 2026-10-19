# EMA Hourly Continuation — FIL/USDT P34_50

**Symbol:** FIL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.3670 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -8.6817 |
| sortino_ratio | -3.7307 |
| max_drawdown | 0.9909 |
| cagr | -0.8444 |
| net_avg_win | 14.2190 |
| net_avg_loss | -31.3647 |
| avg_hold_time_bars | 2.3721 |
| exposure | 0.0974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
