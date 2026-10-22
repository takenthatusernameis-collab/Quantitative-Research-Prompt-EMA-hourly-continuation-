# EMA Hourly Continuation — FLOKI/USDT P89_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5879 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9771 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -4.0905 |
| sortino_ratio | -1.2506 |
| max_drawdown | 0.8030 |
| cagr | -0.4640 |
| net_avg_win | 49.0650 |
| net_avg_loss | -77.0931 |
| avg_hold_time_bars | 5.5136 |
| exposure | 0.1200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
