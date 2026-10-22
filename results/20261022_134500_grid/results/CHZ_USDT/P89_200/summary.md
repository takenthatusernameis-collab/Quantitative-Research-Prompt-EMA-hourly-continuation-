# EMA Hourly Continuation — CHZ/USDT P89_200

**Symbol:** CHZ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.5781 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8874 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -3.1000 |
| sortino_ratio | -0.8199 |
| max_drawdown | 0.6307 |
| cagr | -0.3224 |
| net_avg_win | 52.7608 |
| net_avg_loss | -78.2257 |
| avg_hold_time_bars | 12.5755 |
| exposure | 0.2006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
