# EMA Hourly Continuation — OSMO/USDT P34_144

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.7562 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0856 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -2.0795 |
| sortino_ratio | -0.6372 |
| max_drawdown | 0.5976 |
| cagr | -0.2595 |
| net_avg_win | 69.3280 |
| net_avg_loss | -94.4709 |
| avg_hold_time_bars | 19.3619 |
| exposure | 0.4110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
