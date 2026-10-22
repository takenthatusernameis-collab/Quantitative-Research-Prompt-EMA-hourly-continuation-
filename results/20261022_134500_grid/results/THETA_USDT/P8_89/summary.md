# EMA Hourly Continuation — THETA/USDT P8_89

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -3.3645 |
| sortino_ratio | -1.2149 |
| max_drawdown | 0.7797 |
| cagr | -0.4404 |
| net_avg_win | 49.7271 |
| net_avg_loss | -68.7283 |
| avg_hold_time_bars | 22.0760 |
| exposure | 0.6603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
