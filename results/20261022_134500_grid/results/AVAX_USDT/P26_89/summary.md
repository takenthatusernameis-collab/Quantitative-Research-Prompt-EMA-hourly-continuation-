# EMA Hourly Continuation — AVAX/USDT P26_89

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 1.1065 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -3.9937 |
| sortino_ratio | -1.4287 |
| max_drawdown | 0.8413 |
| cagr | -0.4991 |
| net_avg_win | 55.8662 |
| net_avg_loss | -78.8970 |
| avg_hold_time_bars | 9.8203 |
| exposure | 0.2906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
