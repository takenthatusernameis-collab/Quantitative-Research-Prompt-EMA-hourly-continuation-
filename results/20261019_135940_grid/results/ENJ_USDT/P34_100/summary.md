# EMA Hourly Continuation — ENJ/USDT P34_100

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6490 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 1.0522 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -3.5193 |
| sortino_ratio | -1.2631 |
| max_drawdown | 0.7901 |
| cagr | -0.4503 |
| net_avg_win | 45.3567 |
| net_avg_loss | -67.9533 |
| avg_hold_time_bars | 10.4137 |
| exposure | 0.3044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
