# EMA Hourly Continuation — SHIB/USDT P12_21

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1474 |
| net_profit_factor | 0.2291 |
| net_win_rate | 0.3955 |
| gross_profit_factor | 0.7396 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -14.7556 |
| sortino_ratio | -8.1491 |
| max_drawdown | 1.0000 |
| cagr | -0.9870 |
| net_avg_win | 5.0984 |
| net_avg_loss | -14.5591 |
| avg_hold_time_bars | 2.1045 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
