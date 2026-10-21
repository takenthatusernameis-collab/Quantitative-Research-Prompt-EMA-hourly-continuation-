# EMA Hourly Continuation — CHZ/USDT P50_89

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0721 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.4697 |
| sortino_ratio | -0.3828 |
| max_drawdown | 0.3765 |
| cagr | -0.1615 |
| net_avg_win | 71.6633 |
| net_avg_loss | -98.6570 |
| avg_hold_time_bars | 7.7409 |
| exposure | 0.1154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
