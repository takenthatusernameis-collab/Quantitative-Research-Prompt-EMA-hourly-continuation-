# EMA Hourly Continuation — ETN/USDT P34_55

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.5705 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.7682 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -2.8242 |
| sortino_ratio | -0.6771 |
| max_drawdown | 0.4853 |
| cagr | -0.2676 |
| net_avg_win | 60.7467 |
| net_avg_loss | -84.0688 |
| avg_hold_time_bars | 6.3950 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
