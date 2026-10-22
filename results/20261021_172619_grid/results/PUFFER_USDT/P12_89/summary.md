# EMA Hourly Continuation — PUFFER/USDT P12_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.9256 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.0977 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -0.4877 |
| sortino_ratio | -0.1560 |
| max_drawdown | 0.2370 |
| cagr | -0.0753 |
| net_avg_win | 87.3529 |
| net_avg_loss | -104.4185 |
| avg_hold_time_bars | 24.5152 |
| exposure | 0.5494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
