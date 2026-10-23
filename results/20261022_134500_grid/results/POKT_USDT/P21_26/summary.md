# EMA Hourly Continuation — POKT/USDT P21_26

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.2759 |
| net_win_rate | 0.2969 |
| gross_profit_factor | 0.8167 |
| gross_win_rate | 0.3561 |
| sharpe_ratio | -15.5796 |
| sortino_ratio | -7.8263 |
| max_drawdown | 1.0000 |
| cagr | -0.9836 |
| net_avg_win | 10.5544 |
| net_avg_loss | -16.1519 |
| avg_hold_time_bars | 2.9474 |
| exposure | 0.1622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
