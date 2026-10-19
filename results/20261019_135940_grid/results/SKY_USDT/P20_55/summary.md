# EMA Hourly Continuation — SKY/USDT P20_55

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.4721 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8675 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -6.9760 |
| sortino_ratio | -3.0104 |
| max_drawdown | 0.9511 |
| cagr | -0.7698 |
| net_avg_win | 24.4299 |
| net_avg_loss | -43.1822 |
| avg_hold_time_bars | 6.1216 |
| exposure | 0.2611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
