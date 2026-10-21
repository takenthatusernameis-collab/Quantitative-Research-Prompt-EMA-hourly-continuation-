# EMA Hourly Continuation — SKY/USDT P20_50

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.2455 |
| sortino_ratio | -1.1235 |
| max_drawdown | 0.6668 |
| cagr | -0.4020 |
| net_avg_win | 50.8340 |
| net_avg_loss | -73.6881 |
| avg_hold_time_bars | 7.3543 |
| exposure | 0.1956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
