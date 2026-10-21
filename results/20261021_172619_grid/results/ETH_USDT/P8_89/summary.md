# EMA Hourly Continuation — ETH/USDT P8_89

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.7249 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.0537 |
| sortino_ratio | -0.6125 |
| max_drawdown | 0.5259 |
| cagr | -0.2448 |
| net_avg_win | 61.7329 |
| net_avg_loss | -84.3764 |
| avg_hold_time_bars | 30.9032 |
| exposure | 0.6096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
