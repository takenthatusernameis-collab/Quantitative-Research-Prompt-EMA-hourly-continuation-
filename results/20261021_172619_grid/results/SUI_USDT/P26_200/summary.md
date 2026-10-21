# EMA Hourly Continuation — SUI/USDT P26_200

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.9554 |
| net_win_rate | 0.5292 |
| gross_profit_factor | 1.1165 |
| gross_win_rate | 0.5292 |
| sharpe_ratio | -0.1738 |
| sortino_ratio | -0.0402 |
| max_drawdown | 0.1802 |
| cagr | -0.0224 |
| net_avg_win | 87.0969 |
| net_avg_loss | -102.4647 |
| avg_hold_time_bars | 50.4008 |
| exposure | 0.5888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
