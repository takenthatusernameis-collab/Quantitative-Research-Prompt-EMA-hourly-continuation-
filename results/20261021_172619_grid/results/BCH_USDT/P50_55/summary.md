# EMA Hourly Continuation — BCH/USDT P50_55

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.6374 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -1.3726 |
| sortino_ratio | -0.2044 |
| max_drawdown | 0.2281 |
| cagr | -0.0883 |
| net_avg_win | 68.7559 |
| net_avg_loss | -105.8638 |
| avg_hold_time_bars | 5.0841 |
| exposure | 0.0247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
