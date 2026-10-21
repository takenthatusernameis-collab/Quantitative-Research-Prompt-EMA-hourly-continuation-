# EMA Hourly Continuation — SUPER/USDT P12_144

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.9473 |
| net_win_rate | 0.5308 |
| gross_profit_factor | 1.1216 |
| gross_win_rate | 0.5308 |
| sharpe_ratio | -0.2776 |
| sortino_ratio | -0.0773 |
| max_drawdown | 0.2618 |
| cagr | -0.0404 |
| net_avg_win | 89.1483 |
| net_avg_loss | -106.4802 |
| avg_hold_time_bars | 38.9598 |
| exposure | 0.6605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
