# EMA Hourly Continuation — OSMO/USDT P55_144

**Symbol:** OSMO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5880 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.5769 |
| sortino_ratio | -1.0732 |
| max_drawdown | 0.7291 |
| cagr | -0.3995 |
| net_avg_win | 48.8468 |
| net_avg_loss | -72.7340 |
| avg_hold_time_bars | 12.4845 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
