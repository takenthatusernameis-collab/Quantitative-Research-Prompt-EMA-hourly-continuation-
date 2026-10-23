# EMA Hourly Continuation — YFI/USDT P20_200

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -3.0566 |
| sortino_ratio | -0.8702 |
| max_drawdown | 0.6847 |
| cagr | -0.3428 |
| net_avg_win | 50.5441 |
| net_avg_loss | -78.1263 |
| avg_hold_time_bars | 34.9225 |
| exposure | 0.6527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
