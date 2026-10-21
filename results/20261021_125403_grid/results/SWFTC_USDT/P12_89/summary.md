# EMA Hourly Continuation — SWFTC/USDT P12_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.0165 |
| sortino_ratio | -0.6684 |
| max_drawdown | 0.5450 |
| cagr | -0.2644 |
| net_avg_win | 66.8909 |
| net_avg_loss | -81.8412 |
| avg_hold_time_bars | 17.4148 |
| exposure | 0.4275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
