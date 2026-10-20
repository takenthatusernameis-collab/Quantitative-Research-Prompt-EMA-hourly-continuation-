# EMA Hourly Continuation — SKL/USDT P12_55

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.6706 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -5.0695 |
| sortino_ratio | -2.3075 |
| max_drawdown | 0.9399 |
| cagr | -0.6678 |
| net_avg_win | 37.6385 |
| net_avg_loss | -52.9879 |
| avg_hold_time_bars | 8.3372 |
| exposure | 0.3956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
