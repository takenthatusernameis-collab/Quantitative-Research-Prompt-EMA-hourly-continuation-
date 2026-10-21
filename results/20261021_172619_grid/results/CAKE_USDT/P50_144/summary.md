# EMA Hourly Continuation — CAKE/USDT P50_144

**Symbol:** CAKE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -1.4417 |
| sortino_ratio | -0.3609 |
| max_drawdown | 0.3926 |
| cagr | -0.1530 |
| net_avg_win | 70.7396 |
| net_avg_loss | -95.8294 |
| avg_hold_time_bars | 19.3311 |
| exposure | 0.2680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
