# EMA Hourly Continuation — ZEN/USDT P34_144

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8460 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.3291 |
| sortino_ratio | -0.6388 |
| max_drawdown | 0.5564 |
| cagr | -0.2558 |
| net_avg_win | 69.1277 |
| net_avg_loss | -83.2804 |
| avg_hold_time_bars | 24.4973 |
| exposure | 0.4165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
