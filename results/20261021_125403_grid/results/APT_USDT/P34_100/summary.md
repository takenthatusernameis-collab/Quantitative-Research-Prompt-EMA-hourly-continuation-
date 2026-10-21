# EMA Hourly Continuation — APT/USDT P34_100

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0335 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.2798 |
| sortino_ratio | -0.3667 |
| max_drawdown | 0.3688 |
| cagr | -0.1563 |
| net_avg_win | 73.1742 |
| net_avg_loss | -93.9898 |
| avg_hold_time_bars | 13.9799 |
| exposure | 0.2529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
