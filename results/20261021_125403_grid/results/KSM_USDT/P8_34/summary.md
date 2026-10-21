# EMA Hourly Continuation — KSM/USDT P8_34

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.6487 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.8243 |
| sortino_ratio | -1.5399 |
| max_drawdown | 0.8338 |
| cagr | -0.5067 |
| net_avg_win | 41.0103 |
| net_avg_loss | -55.8930 |
| avg_hold_time_bars | 8.4015 |
| exposure | 0.3044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
