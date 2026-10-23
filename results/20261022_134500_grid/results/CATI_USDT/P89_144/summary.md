# EMA Hourly Continuation — CATI/USDT P89_144

**Symbol:** CATI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.4846 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -5.4248 |
| sortino_ratio | -1.8153 |
| max_drawdown | 0.8382 |
| cagr | -0.5812 |
| net_avg_win | 38.5627 |
| net_avg_loss | -62.9240 |
| avg_hold_time_bars | 5.7424 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
