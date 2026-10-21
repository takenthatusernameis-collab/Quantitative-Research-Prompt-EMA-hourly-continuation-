# EMA Hourly Continuation — BCH/USDT P8_100

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.8198 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0633 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.4343 |
| sortino_ratio | -0.4348 |
| max_drawdown | 0.4739 |
| cagr | -0.1822 |
| net_avg_win | 79.1063 |
| net_avg_loss | -100.9236 |
| avg_hold_time_bars | 31.5628 |
| exposure | 0.6399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
