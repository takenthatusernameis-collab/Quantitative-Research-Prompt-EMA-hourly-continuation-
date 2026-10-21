# EMA Hourly Continuation — BAT/USDT P20_26

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.5244 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.5645 |
| sortino_ratio | -0.8992 |
| max_drawdown | 0.6494 |
| cagr | -0.3398 |
| net_avg_win | 50.2877 |
| net_avg_loss | -82.0261 |
| avg_hold_time_bars | 4.4838 |
| exposure | 0.0628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
