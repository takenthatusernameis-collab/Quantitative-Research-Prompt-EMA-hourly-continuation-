# EMA Hourly Continuation — CSPR/USDT P12_200

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6943 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.8411 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -2.4000 |
| sortino_ratio | -0.7098 |
| max_drawdown | 0.5705 |
| cagr | -0.2789 |
| net_avg_win | 63.9198 |
| net_avg_loss | -77.3030 |
| avg_hold_time_bars | 32.6514 |
| exposure | 0.6471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
