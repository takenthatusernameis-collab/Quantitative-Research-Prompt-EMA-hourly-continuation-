# EMA Hourly Continuation — NMR/USDT P20_200

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6482 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.8860 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.5802 |
| sortino_ratio | -0.7655 |
| max_drawdown | 0.6138 |
| cagr | -0.2986 |
| net_avg_win | 52.7284 |
| net_avg_loss | -72.2325 |
| avg_hold_time_bars | 31.5662 |
| exposure | 0.6285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
