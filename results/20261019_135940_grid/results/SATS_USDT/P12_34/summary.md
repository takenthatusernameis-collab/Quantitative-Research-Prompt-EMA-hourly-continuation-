# EMA Hourly Continuation — SATS/USDT P12_34

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.5702 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -5.9191 |
| sortino_ratio | -2.7432 |
| max_drawdown | 0.9657 |
| cagr | -0.7344 |
| net_avg_win | 25.0913 |
| net_avg_loss | -38.6960 |
| avg_hold_time_bars | 4.9743 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
