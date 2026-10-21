# EMA Hourly Continuation — ENS/USDT P26_34

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.7288 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0700 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.4043 |
| sortino_ratio | -0.2833 |
| max_drawdown | 0.3027 |
| cagr | -0.1226 |
| net_avg_win | 73.7472 |
| net_avg_loss | -108.6500 |
| avg_hold_time_bars | 5.1827 |
| exposure | 0.0464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
