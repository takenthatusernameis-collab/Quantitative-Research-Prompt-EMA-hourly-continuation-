# EMA Hourly Continuation — ENS/USDT P20_89

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8106 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0280 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.5656 |
| sortino_ratio | -0.5030 |
| max_drawdown | 0.5267 |
| cagr | -0.2078 |
| net_avg_win | 74.6187 |
| net_avg_loss | -94.2804 |
| avg_hold_time_bars | 17.4701 |
| exposure | 0.3986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
