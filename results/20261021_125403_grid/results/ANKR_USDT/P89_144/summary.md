# EMA Hourly Continuation — ANKR/USDT P89_144

**Symbol:** ANKR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.5980 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8417 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.8279 |
| sortino_ratio | -0.7193 |
| max_drawdown | 0.5649 |
| cagr | -0.2821 |
| net_avg_win | 57.5652 |
| net_avg_loss | -82.1844 |
| avg_hold_time_bars | 11.5363 |
| exposure | 0.1662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
