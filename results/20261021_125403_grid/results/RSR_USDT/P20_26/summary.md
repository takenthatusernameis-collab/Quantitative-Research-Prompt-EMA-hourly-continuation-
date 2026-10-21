# EMA Hourly Continuation — RSR/USDT P20_26

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.8123 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.0986 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -0.8684 |
| sortino_ratio | -0.1778 |
| max_drawdown | 0.2269 |
| cagr | -0.0787 |
| net_avg_win | 75.9593 |
| net_avg_loss | -104.3380 |
| avg_hold_time_bars | 4.8358 |
| exposure | 0.0442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
