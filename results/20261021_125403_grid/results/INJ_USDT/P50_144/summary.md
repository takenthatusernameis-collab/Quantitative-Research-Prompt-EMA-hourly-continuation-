# EMA Hourly Continuation — INJ/USDT P50_144

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -1.5955 |
| sortino_ratio | -0.4233 |
| max_drawdown | 0.3967 |
| cagr | -0.1768 |
| net_avg_win | 69.7900 |
| net_avg_loss | -85.8334 |
| avg_hold_time_bars | 14.1561 |
| exposure | 0.2226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
