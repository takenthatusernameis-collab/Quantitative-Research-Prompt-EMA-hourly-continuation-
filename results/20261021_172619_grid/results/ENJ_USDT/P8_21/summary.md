# EMA Hourly Continuation — ENJ/USDT P8_21

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7488 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0350 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.3010 |
| sortino_ratio | -0.8141 |
| max_drawdown | 0.6304 |
| cagr | -0.3118 |
| net_avg_win | 58.8862 |
| net_avg_loss | -81.2695 |
| avg_hold_time_bars | 6.0115 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
