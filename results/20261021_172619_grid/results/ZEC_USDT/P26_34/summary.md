# EMA Hourly Continuation — ZEC/USDT P26_34

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 131 |
| net_profit_factor | 0.7410 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.0485 |
| sortino_ratio | -0.1721 |
| max_drawdown | 0.1959 |
| cagr | -0.0762 |
| net_avg_win | 79.4120 |
| net_avg_loss | -105.5465 |
| avg_hold_time_bars | 5.5038 |
| exposure | 0.0328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
