# EMA Hourly Continuation — DUSK/USDT P50_144

**Symbol:** DUSK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6415 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.9280 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.8747 |
| sortino_ratio | -0.8903 |
| max_drawdown | 0.6592 |
| cagr | -0.3413 |
| net_avg_win | 51.4389 |
| net_avg_loss | -71.6234 |
| avg_hold_time_bars | 12.9812 |
| exposure | 0.2826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
