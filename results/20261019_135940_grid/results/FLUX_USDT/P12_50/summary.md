# EMA Hourly Continuation — FLUX/USDT P12_50

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.5475 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9166 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -6.2429 |
| sortino_ratio | -2.9179 |
| max_drawdown | 0.9737 |
| cagr | -0.7610 |
| net_avg_win | 22.3305 |
| net_avg_loss | -36.6159 |
| avg_hold_time_bars | 6.3662 |
| exposure | 0.3224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
