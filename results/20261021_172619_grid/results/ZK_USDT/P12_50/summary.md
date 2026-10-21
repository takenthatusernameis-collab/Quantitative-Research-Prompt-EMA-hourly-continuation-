# EMA Hourly Continuation — ZK/USDT P12_50

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.8319 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0367 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.6799 |
| sortino_ratio | -0.6241 |
| max_drawdown | 0.5772 |
| cagr | -0.2509 |
| net_avg_win | 76.9825 |
| net_avg_loss | -94.3295 |
| avg_hold_time_bars | 10.3914 |
| exposure | 0.3171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
