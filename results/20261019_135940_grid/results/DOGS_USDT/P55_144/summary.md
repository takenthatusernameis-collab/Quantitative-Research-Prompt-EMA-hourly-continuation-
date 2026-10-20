# EMA Hourly Continuation — DOGS/USDT P55_144

**Symbol:** DOGS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7219 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 1.0519 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -2.6292 |
| sortino_ratio | -0.8151 |
| max_drawdown | 0.5895 |
| cagr | -0.3229 |
| net_avg_win | 71.5416 |
| net_avg_loss | -97.6836 |
| avg_hold_time_bars | 12.4530 |
| exposure | 0.2742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
