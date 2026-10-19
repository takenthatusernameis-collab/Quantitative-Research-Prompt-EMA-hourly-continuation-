# EMA Hourly Continuation — APE/USDT P26_100

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5691 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.8765 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -3.9527 |
| sortino_ratio | -1.4207 |
| max_drawdown | 0.8233 |
| cagr | -0.4874 |
| net_avg_win | 35.2188 |
| net_avg_loss | -55.6776 |
| avg_hold_time_bars | 12.3447 |
| exposure | 0.3614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
