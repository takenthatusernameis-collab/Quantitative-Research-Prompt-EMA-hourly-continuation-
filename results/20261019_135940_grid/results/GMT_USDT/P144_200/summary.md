# EMA Hourly Continuation — GMT/USDT P144_200

**Symbol:** GMT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5575 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -3.3958 |
| sortino_ratio | -0.9499 |
| max_drawdown | 0.6834 |
| cagr | -0.3674 |
| net_avg_win | 43.9337 |
| net_avg_loss | -78.8012 |
| avg_hold_time_bars | 4.5153 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
