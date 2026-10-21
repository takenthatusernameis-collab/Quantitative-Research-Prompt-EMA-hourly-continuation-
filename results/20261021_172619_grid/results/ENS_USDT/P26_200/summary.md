# EMA Hourly Continuation — ENS/USDT P26_200

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.8464 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -0.7745 |
| sortino_ratio | -0.1768 |
| max_drawdown | 0.2601 |
| cagr | -0.0799 |
| net_avg_win | 81.2186 |
| net_avg_loss | -97.4773 |
| avg_hold_time_bars | 53.5906 |
| exposure | 0.6187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
