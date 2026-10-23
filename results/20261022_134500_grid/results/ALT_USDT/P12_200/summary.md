# EMA Hourly Continuation — ALT/USDT P12_200

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.1224 |
| sortino_ratio | -0.5800 |
| max_drawdown | 0.5255 |
| cagr | -0.2398 |
| net_avg_win | 66.5063 |
| net_avg_loss | -87.3625 |
| avg_hold_time_bars | 43.8209 |
| exposure | 0.7450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
