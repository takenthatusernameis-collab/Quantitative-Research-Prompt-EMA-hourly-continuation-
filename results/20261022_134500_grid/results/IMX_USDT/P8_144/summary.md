# EMA Hourly Continuation — IMX/USDT P8_144

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7461 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0284 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -1.7840 |
| sortino_ratio | -0.5617 |
| max_drawdown | 0.5146 |
| cagr | -0.2332 |
| net_avg_win | 56.4703 |
| net_avg_loss | -80.1034 |
| avg_hold_time_bars | 33.3806 |
| exposure | 0.7462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
