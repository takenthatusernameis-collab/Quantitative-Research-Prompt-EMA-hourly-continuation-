# EMA Hourly Continuation — ENJ/USDT P21_34

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6848 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.1810 |
| sortino_ratio | -0.5609 |
| max_drawdown | 0.5120 |
| cagr | -0.2255 |
| net_avg_win | 64.5104 |
| net_avg_loss | -93.6225 |
| avg_hold_time_bars | 4.6573 |
| exposure | 0.0677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
