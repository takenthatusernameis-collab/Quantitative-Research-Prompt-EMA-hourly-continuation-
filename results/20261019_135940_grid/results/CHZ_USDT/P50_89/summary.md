# EMA Hourly Continuation — CHZ/USDT P50_89

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.5046 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 1.0236 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -5.4430 |
| sortino_ratio | -1.9450 |
| max_drawdown | 0.9119 |
| cagr | -0.6155 |
| net_avg_win | 30.1688 |
| net_avg_loss | -55.1199 |
| avg_hold_time_bars | 4.7812 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
