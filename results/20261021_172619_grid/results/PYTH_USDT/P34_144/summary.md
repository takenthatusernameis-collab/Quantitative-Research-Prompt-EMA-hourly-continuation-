# EMA Hourly Continuation — PYTH/USDT P34_144

**Symbol:** PYTH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8470 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0081 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -0.9418 |
| sortino_ratio | -0.2536 |
| max_drawdown | 0.3391 |
| cagr | -0.1122 |
| net_avg_win | 80.3356 |
| net_avg_loss | -96.4725 |
| avg_hold_time_bars | 24.1501 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
