# EMA Hourly Continuation — ZPAY/USDT P26_34

**Symbol:** ZPAY/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.2765 |
| net_win_rate | 0.3177 |
| gross_profit_factor | 0.5504 |
| gross_win_rate | 0.3289 |
| sharpe_ratio | -10.8020 |
| sortino_ratio | -4.5440 |
| max_drawdown | 0.9963 |
| cagr | -0.8910 |
| net_avg_win | 13.4082 |
| net_avg_loss | -22.5748 |
| avg_hold_time_bars | 5.1320 |
| exposure | 0.2076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
