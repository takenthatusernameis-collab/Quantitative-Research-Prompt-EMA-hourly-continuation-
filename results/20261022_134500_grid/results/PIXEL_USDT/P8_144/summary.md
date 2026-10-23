# EMA Hourly Continuation — PIXEL/USDT P8_144

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 1.0268 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -2.0271 |
| sortino_ratio | -0.5836 |
| max_drawdown | 0.5676 |
| cagr | -0.2418 |
| net_avg_win | 74.4101 |
| net_avg_loss | -95.6557 |
| avg_hold_time_bars | 42.1775 |
| exposure | 0.7959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
