# EMA Hourly Continuation — FLOKI/USDT P34_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8686 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0511 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -0.7837 |
| sortino_ratio | -0.2108 |
| max_drawdown | 0.2669 |
| cagr | -0.0947 |
| net_avg_win | 81.2046 |
| net_avg_loss | -98.9887 |
| avg_hold_time_bars | 27.2343 |
| exposure | 0.4333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
