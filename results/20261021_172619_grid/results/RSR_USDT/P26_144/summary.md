# EMA Hourly Continuation — RSR/USDT P26_144

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.9141 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0792 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -0.5138 |
| sortino_ratio | -0.1446 |
| max_drawdown | 0.2468 |
| cagr | -0.0686 |
| net_avg_win | 87.3226 |
| net_avg_loss | -103.3215 |
| avg_hold_time_bars | 24.7676 |
| exposure | 0.4312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
