# EMA Hourly Continuation — OSMO/USDT P12_200

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7779 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0692 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.6636 |
| sortino_ratio | -0.4621 |
| max_drawdown | 0.4894 |
| cagr | -0.1965 |
| net_avg_win | 76.3458 |
| net_avg_loss | -100.2047 |
| avg_hold_time_bars | 41.5703 |
| exposure | 0.7256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
