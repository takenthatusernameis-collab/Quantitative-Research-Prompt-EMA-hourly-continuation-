# EMA Hourly Continuation — ALT/USDT P20_50

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -6.0258 |
| sortino_ratio | -2.5035 |
| max_drawdown | 0.9538 |
| cagr | -0.6984 |
| net_avg_win | 30.7520 |
| net_avg_loss | -44.4158 |
| avg_hold_time_bars | 6.0414 |
| exposure | 0.2386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
