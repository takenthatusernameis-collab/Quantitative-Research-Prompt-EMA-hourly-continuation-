# EMA Hourly Continuation — TWT/USDT P20_55

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.7228 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -2.1391 |
| sortino_ratio | -0.7492 |
| max_drawdown | 0.6257 |
| cagr | -0.2896 |
| net_avg_win | 48.6168 |
| net_avg_loss | -74.4987 |
| avg_hold_time_bars | 8.0969 |
| exposure | 0.2164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
