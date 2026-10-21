# EMA Hourly Continuation — WEMIX/USDT P20_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.7773 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -3.1432 |
| sortino_ratio | -0.8546 |
| max_drawdown | 0.6342 |
| cagr | -0.3272 |
| net_avg_win | 65.2383 |
| net_avg_loss | -79.0344 |
| avg_hold_time_bars | 34.5054 |
| exposure | 0.5803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
