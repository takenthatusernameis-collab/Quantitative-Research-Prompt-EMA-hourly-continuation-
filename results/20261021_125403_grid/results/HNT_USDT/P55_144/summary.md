# EMA Hourly Continuation — HNT/USDT P55_144

**Symbol:** HNT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8207 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.0711 |
| sortino_ratio | -0.5683 |
| max_drawdown | 0.5595 |
| cagr | -0.2301 |
| net_avg_win | 57.2589 |
| net_avg_loss | -74.2584 |
| avg_hold_time_bars | 14.9491 |
| exposure | 0.2535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
