# EMA Hourly Continuation — SKL/USDT P20_144

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -2.1075 |
| sortino_ratio | -0.6296 |
| max_drawdown | 0.5788 |
| cagr | -0.2605 |
| net_avg_win | 66.5247 |
| net_avg_loss | -90.4375 |
| avg_hold_time_bars | 27.8958 |
| exposure | 0.5719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
