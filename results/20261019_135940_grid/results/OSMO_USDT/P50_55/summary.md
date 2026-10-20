# EMA Hourly Continuation — OSMO/USDT P50_55

**Symbol:** OSMO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.1866 |
| net_win_rate | 0.3175 |
| gross_profit_factor | 0.7556 |
| gross_win_rate | 0.3856 |
| sharpe_ratio | -13.1372 |
| sortino_ratio | -5.5963 |
| max_drawdown | 0.9994 |
| cagr | -0.9495 |
| net_avg_win | 8.7845 |
| net_avg_loss | -21.9023 |
| avg_hold_time_bars | 2.4939 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
