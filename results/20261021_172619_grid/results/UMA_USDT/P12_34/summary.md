# EMA Hourly Continuation — UMA/USDT P12_34

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6212 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -3.8257 |
| sortino_ratio | -1.4110 |
| max_drawdown | 0.8130 |
| cagr | -0.4771 |
| net_avg_win | 41.4416 |
| net_avg_loss | -60.7904 |
| avg_hold_time_bars | 6.8006 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
