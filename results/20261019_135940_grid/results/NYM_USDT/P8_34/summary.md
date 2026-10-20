# EMA Hourly Continuation — NYM/USDT P8_34

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.3087 |
| net_win_rate | 0.3848 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -12.1860 |
| sortino_ratio | -5.7355 |
| max_drawdown | 0.9996 |
| cagr | -0.9541 |
| net_avg_win | 10.5280 |
| net_avg_loss | -21.3267 |
| avg_hold_time_bars | 8.8376 |
| exposure | 0.4427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
