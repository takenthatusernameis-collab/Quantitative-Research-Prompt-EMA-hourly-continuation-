# EMA Hourly Continuation — DOGE/USDT P34_55

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.3342 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.7917 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -9.7547 |
| sortino_ratio | -4.0887 |
| max_drawdown | 0.9953 |
| cagr | -0.8807 |
| net_avg_win | 13.8746 |
| net_avg_loss | -29.4229 |
| avg_hold_time_bars | 3.0853 |
| exposure | 0.1217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
