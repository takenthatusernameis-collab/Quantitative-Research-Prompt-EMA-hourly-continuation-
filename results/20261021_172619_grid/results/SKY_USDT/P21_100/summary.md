# EMA Hourly Continuation — SKY/USDT P21_100

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8496 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0751 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -1.0589 |
| sortino_ratio | -0.3220 |
| max_drawdown | 0.4588 |
| cagr | -0.1399 |
| net_avg_win | 78.8981 |
| net_avg_loss | -100.8262 |
| avg_hold_time_bars | 22.4658 |
| exposure | 0.4572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
