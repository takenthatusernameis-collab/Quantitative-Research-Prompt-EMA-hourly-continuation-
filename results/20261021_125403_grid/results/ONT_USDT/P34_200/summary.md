# EMA Hourly Continuation — ONT/USDT P34_200

**Symbol:** ONT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7923 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.2668 |
| sortino_ratio | -0.3186 |
| max_drawdown | 0.4005 |
| cagr | -0.1373 |
| net_avg_win | 77.5370 |
| net_avg_loss | -94.7662 |
| avg_hold_time_bars | 32.7556 |
| exposure | 0.4610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
