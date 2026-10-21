# EMA Hourly Continuation — DOGS/USDT P20_200

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8854 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -0.6514 |
| sortino_ratio | -0.1701 |
| max_drawdown | 0.2333 |
| cagr | -0.0783 |
| net_avg_win | 85.7053 |
| net_avg_loss | -100.9757 |
| avg_hold_time_bars | 39.7711 |
| exposure | 0.5992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
