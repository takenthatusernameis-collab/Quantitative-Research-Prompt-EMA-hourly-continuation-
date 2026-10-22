# EMA Hourly Continuation — TNSR/USDT P50_89

**Symbol:** TNSR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7613 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7874 |
| sortino_ratio | -0.5087 |
| max_drawdown | 0.4793 |
| cagr | -0.2087 |
| net_avg_win | 71.8174 |
| net_avg_loss | -94.3382 |
| avg_hold_time_bars | 7.3030 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
