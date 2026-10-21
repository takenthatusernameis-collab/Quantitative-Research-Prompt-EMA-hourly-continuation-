# EMA Hourly Continuation — CFX/USDT P20_144

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.8218 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0051 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.1727 |
| sortino_ratio | -0.3316 |
| max_drawdown | 0.3681 |
| cagr | -0.1424 |
| net_avg_win | 74.9305 |
| net_avg_loss | -93.0717 |
| avg_hold_time_bars | 28.9385 |
| exposure | 0.5130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
