# EMA Hourly Continuation — CHZ/USDT P12_55

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.8167 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0543 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -1.6086 |
| sortino_ratio | -0.5826 |
| max_drawdown | 0.5195 |
| cagr | -0.2365 |
| net_avg_win | 67.2600 |
| net_avg_loss | -86.8900 |
| avg_hold_time_bars | 12.0976 |
| exposure | 0.3492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
