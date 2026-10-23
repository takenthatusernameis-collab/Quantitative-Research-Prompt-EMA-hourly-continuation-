# EMA Hourly Continuation — IO/USDT P20_89

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8819 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -4.6265 |
| sortino_ratio | -1.7873 |
| max_drawdown | 0.8744 |
| cagr | -0.5791 |
| net_avg_win | 39.2319 |
| net_avg_loss | -56.4744 |
| avg_hold_time_bars | 11.4559 |
| exposure | 0.3965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
