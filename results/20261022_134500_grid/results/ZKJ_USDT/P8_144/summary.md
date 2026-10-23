# EMA Hourly Continuation — ZKJ/USDT P8_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.3072 |
| net_win_rate | 0.4062 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.7948 |
| sortino_ratio | -0.6080 |
| max_drawdown | 0.5756 |
| cagr | -0.2775 |
| net_avg_win | 47.5623 |
| net_avg_loss | -105.9466 |
| avg_hold_time_bars | 160.3281 |
| exposure | 0.9328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
