# EMA Hourly Continuation — G/USDT P100_144

**Symbol:** G/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.3964 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.8383 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -5.7565 |
| sortino_ratio | -1.7767 |
| max_drawdown | 0.8530 |
| cagr | -0.5772 |
| net_avg_win | 31.3805 |
| net_avg_loss | -61.7222 |
| avg_hold_time_bars | 4.7574 |
| exposure | 0.1011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
