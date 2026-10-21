# EMA Hourly Continuation — ORBS/USDT P89_200

**Symbol:** ORBS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -2.9899 |
| sortino_ratio | -0.7538 |
| max_drawdown | 0.5922 |
| cagr | -0.2935 |
| net_avg_win | 63.6619 |
| net_avg_loss | -85.5313 |
| avg_hold_time_bars | 15.9968 |
| exposure | 0.2283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
