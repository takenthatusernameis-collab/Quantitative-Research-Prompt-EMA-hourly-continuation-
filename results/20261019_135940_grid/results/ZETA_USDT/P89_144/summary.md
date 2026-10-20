# EMA Hourly Continuation — ZETA/USDT P89_144

**Symbol:** ZETA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -5.3506 |
| sortino_ratio | -1.7251 |
| max_drawdown | 0.8802 |
| cagr | -0.5620 |
| net_avg_win | 45.0781 |
| net_avg_loss | -62.8053 |
| avg_hold_time_bars | 5.6647 |
| exposure | 0.1330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
