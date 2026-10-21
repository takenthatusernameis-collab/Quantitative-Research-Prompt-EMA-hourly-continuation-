# EMA Hourly Continuation — FLUX/USDT P12_100

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7863 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.5721 |
| sortino_ratio | -0.5151 |
| max_drawdown | 0.4889 |
| cagr | -0.2128 |
| net_avg_win | 63.9171 |
| net_avg_loss | -79.7535 |
| avg_hold_time_bars | 22.8114 |
| exposure | 0.5444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
