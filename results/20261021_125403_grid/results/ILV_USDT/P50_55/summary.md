# EMA Hourly Continuation — ILV/USDT P50_55

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.7829 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1738 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | -0.8912 |
| sortino_ratio | -0.1459 |
| max_drawdown | 0.2327 |
| cagr | -0.0649 |
| net_avg_win | 81.0408 |
| net_avg_loss | -121.0559 |
| avg_hold_time_bars | 5.0312 |
| exposure | 0.0293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
