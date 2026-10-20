# EMA Hourly Continuation — DGB/USDT P20_100

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.5729 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.9094 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -5.4186 |
| sortino_ratio | -2.0893 |
| max_drawdown | 0.9308 |
| cagr | -0.6439 |
| net_avg_win | 35.6578 |
| net_avg_loss | -51.6965 |
| avg_hold_time_bars | 11.7836 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
