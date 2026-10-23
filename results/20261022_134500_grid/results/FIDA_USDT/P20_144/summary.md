# EMA Hourly Continuation — FIDA/USDT P20_144

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.5793 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.9211 |
| sortino_ratio | -1.2680 |
| max_drawdown | 0.7923 |
| cagr | -0.4542 |
| net_avg_win | 45.1010 |
| net_avg_loss | -63.5098 |
| avg_hold_time_bars | 22.7462 |
| exposure | 0.5476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
