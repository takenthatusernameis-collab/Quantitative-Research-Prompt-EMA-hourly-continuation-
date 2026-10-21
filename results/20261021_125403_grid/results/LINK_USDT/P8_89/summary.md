# EMA Hourly Continuation — LINK/USDT P8_89

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.8017 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.6425 |
| sortino_ratio | -0.5223 |
| max_drawdown | 0.4971 |
| cagr | -0.2153 |
| net_avg_win | 74.9205 |
| net_avg_loss | -92.7031 |
| avg_hold_time_bars | 27.6255 |
| exposure | 0.6203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
