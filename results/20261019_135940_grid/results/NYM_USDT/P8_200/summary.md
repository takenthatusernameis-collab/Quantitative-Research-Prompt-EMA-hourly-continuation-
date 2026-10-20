# EMA Hourly Continuation — NYM/USDT P8_200

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.3087 |
| net_win_rate | 0.3307 |
| gross_profit_factor | 0.5447 |
| gross_win_rate | 0.3427 |
| sharpe_ratio | -8.0571 |
| sortino_ratio | -2.5368 |
| max_drawdown | 0.9634 |
| cagr | -0.7299 |
| net_avg_win | 26.0535 |
| net_avg_loss | -41.6926 |
| avg_hold_time_bars | 33.2886 |
| exposure | 0.7550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
