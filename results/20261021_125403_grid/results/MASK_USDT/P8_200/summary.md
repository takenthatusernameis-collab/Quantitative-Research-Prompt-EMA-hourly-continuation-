# EMA Hourly Continuation — MASK/USDT P8_200

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5837 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.7492 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -2.9927 |
| sortino_ratio | -0.8010 |
| max_drawdown | 0.6176 |
| cagr | -0.3106 |
| net_avg_win | 54.5487 |
| net_avg_loss | -72.5338 |
| avg_hold_time_bars | 46.3221 |
| exposure | 0.7517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
