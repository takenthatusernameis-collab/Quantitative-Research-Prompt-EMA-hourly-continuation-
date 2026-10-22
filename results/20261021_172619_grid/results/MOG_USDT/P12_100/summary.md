# EMA Hourly Continuation — MOG/USDT P12_100

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.8339 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.3501 |
| sortino_ratio | -0.4252 |
| max_drawdown | 0.4635 |
| cagr | -0.1799 |
| net_avg_win | 84.6297 |
| net_avg_loss | -96.1701 |
| avg_hold_time_bars | 25.0381 |
| exposure | 0.5551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
