# EMA Hourly Continuation — FLUX/USDT P12_100

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6309 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -3.5597 |
| sortino_ratio | -1.3257 |
| max_drawdown | 0.8075 |
| cagr | -0.4725 |
| net_avg_win | 39.8315 |
| net_avg_loss | -59.8219 |
| avg_hold_time_bars | 17.4511 |
| exposure | 0.5592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
