# EMA Hourly Continuation — MERL/USDT P50_55

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.3008 |
| net_win_rate | 0.3818 |
| gross_profit_factor | 0.6171 |
| gross_win_rate | 0.4055 |
| sharpe_ratio | -9.8139 |
| sortino_ratio | -4.0032 |
| max_drawdown | 0.9937 |
| cagr | -0.8656 |
| net_avg_win | 13.9227 |
| net_avg_loss | -28.5887 |
| avg_hold_time_bars | 2.1306 |
| exposure | 0.0781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
