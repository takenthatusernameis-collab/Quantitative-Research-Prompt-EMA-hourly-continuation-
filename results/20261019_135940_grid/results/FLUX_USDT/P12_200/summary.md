# EMA Hourly Continuation — FLUX/USDT P12_200

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7695 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0747 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -1.4418 |
| sortino_ratio | -0.3967 |
| max_drawdown | 0.3989 |
| cagr | -0.1703 |
| net_avg_win | 66.1130 |
| net_avg_loss | -87.3044 |
| avg_hold_time_bars | 44.3867 |
| exposure | 0.7566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
