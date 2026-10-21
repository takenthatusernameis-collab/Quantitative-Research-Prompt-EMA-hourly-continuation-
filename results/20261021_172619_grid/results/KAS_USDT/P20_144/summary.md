# EMA Hourly Continuation — KAS/USDT P20_144

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.8363 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0226 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.0204 |
| sortino_ratio | -0.2937 |
| max_drawdown | 0.3470 |
| cagr | -0.1284 |
| net_avg_win | 72.4107 |
| net_avg_loss | -90.5349 |
| avg_hold_time_bars | 26.2333 |
| exposure | 0.4805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
