# EMA Hourly Continuation — SAFE/USDT P26_144

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8489 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -0.8472 |
| sortino_ratio | -0.2264 |
| max_drawdown | 0.2770 |
| cagr | -0.1017 |
| net_avg_win | 74.4731 |
| net_avg_loss | -92.4251 |
| avg_hold_time_bars | 33.4725 |
| exposure | 0.5289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
