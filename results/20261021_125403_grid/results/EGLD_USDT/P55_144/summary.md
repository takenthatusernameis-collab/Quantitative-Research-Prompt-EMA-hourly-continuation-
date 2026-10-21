# EMA Hourly Continuation — EGLD/USDT P55_144

**Symbol:** EGLD/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.6402 |
| sortino_ratio | -0.4297 |
| max_drawdown | 0.4120 |
| cagr | -0.1794 |
| net_avg_win | 62.8887 |
| net_avg_loss | -84.0570 |
| avg_hold_time_bars | 16.6269 |
| exposure | 0.2532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
