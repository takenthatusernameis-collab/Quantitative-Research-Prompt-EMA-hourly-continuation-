# EMA Hourly Continuation — AUCTION/USDT P8_21

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.6017 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8887 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -5.7124 |
| sortino_ratio | -2.2632 |
| max_drawdown | 0.9342 |
| cagr | -0.6541 |
| net_avg_win | 40.7730 |
| net_avg_loss | -54.3706 |
| avg_hold_time_bars | 6.2942 |
| exposure | 0.2208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
