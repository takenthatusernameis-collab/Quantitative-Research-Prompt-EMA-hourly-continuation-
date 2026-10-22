# EMA Hourly Continuation — DOGE/USDT P12_100

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9050 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -5.1689 |
| sortino_ratio | -1.8706 |
| max_drawdown | 0.9109 |
| cagr | -0.6087 |
| net_avg_win | 35.8828 |
| net_avg_loss | -55.0212 |
| avg_hold_time_bars | 17.8279 |
| exposure | 0.5510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
