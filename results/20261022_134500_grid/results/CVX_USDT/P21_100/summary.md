# EMA Hourly Continuation — CVX/USDT P21_100

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6318 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.8390 |
| sortino_ratio | -1.4064 |
| max_drawdown | 0.8177 |
| cagr | -0.4842 |
| net_avg_win | 44.2815 |
| net_avg_loss | -61.4735 |
| avg_hold_time_bars | 12.4420 |
| exposure | 0.3800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
