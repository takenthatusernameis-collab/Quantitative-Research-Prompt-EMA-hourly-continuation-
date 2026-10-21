# EMA Hourly Continuation — FLOKI/USDT P55_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8596 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -0.8063 |
| sortino_ratio | -0.1931 |
| max_drawdown | 0.2501 |
| cagr | -0.0867 |
| net_avg_win | 88.4775 |
| net_avg_loss | -105.1676 |
| avg_hold_time_bars | 31.9211 |
| exposure | 0.4048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
