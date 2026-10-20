# EMA Hourly Continuation — ENJ/USDT P26_144

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9870 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -2.6864 |
| sortino_ratio | -0.8317 |
| max_drawdown | 0.6586 |
| cagr | -0.3288 |
| net_avg_win | 57.3540 |
| net_avg_loss | -81.2020 |
| avg_hold_time_bars | 22.8719 |
| exposure | 0.5032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
