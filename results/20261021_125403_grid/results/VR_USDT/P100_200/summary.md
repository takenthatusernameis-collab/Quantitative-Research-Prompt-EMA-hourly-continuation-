# EMA Hourly Continuation — VR/USDT P100_200

**Symbol:** VR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.5072 |
| net_win_rate | 0.3728 |
| gross_profit_factor | 0.6128 |
| gross_win_rate | 0.3728 |
| sharpe_ratio | -3.3446 |
| sortino_ratio | -0.7086 |
| max_drawdown | 0.5638 |
| cagr | -0.2814 |
| net_avg_win | 68.2814 |
| net_avg_loss | -80.0146 |
| avg_hold_time_bars | 13.9781 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
