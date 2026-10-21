# EMA Hourly Continuation — ETC/USDT P34_50

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.5067 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.8113 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -3.3046 |
| sortino_ratio | -0.7422 |
| max_drawdown | 0.5779 |
| cagr | -0.2884 |
| net_avg_win | 54.1230 |
| net_avg_loss | -85.6162 |
| avg_hold_time_bars | 4.8735 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
