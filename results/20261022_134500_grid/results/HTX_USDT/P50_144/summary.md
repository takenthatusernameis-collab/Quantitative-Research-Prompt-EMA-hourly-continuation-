# EMA Hourly Continuation — HTX/USDT P50_144

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.3125 |
| net_win_rate | 0.3216 |
| gross_profit_factor | 0.7582 |
| gross_win_rate | 0.3799 |
| sharpe_ratio | -10.1617 |
| sortino_ratio | -3.5192 |
| max_drawdown | 0.9912 |
| cagr | -0.8448 |
| net_avg_win | 24.7439 |
| net_avg_loss | -37.5324 |
| avg_hold_time_bars | 12.2721 |
| exposure | 0.3143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
