# EMA Hourly Continuation — SLP/USDT P26_200

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8435 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.0654 |
| sortino_ratio | -0.2884 |
| max_drawdown | 0.3689 |
| cagr | -0.1264 |
| net_avg_win | 85.6965 |
| net_avg_loss | -104.4809 |
| avg_hold_time_bars | 34.0140 |
| exposure | 0.5520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
