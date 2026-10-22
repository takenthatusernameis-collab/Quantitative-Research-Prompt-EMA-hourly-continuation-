# EMA Hourly Continuation — TNSR/USDT P20_34

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7460 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0409 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -2.1246 |
| sortino_ratio | -0.6318 |
| max_drawdown | 0.5551 |
| cagr | -0.2513 |
| net_avg_win | 69.8038 |
| net_avg_loss | -95.7645 |
| avg_hold_time_bars | 4.7030 |
| exposure | 0.0917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
