# EMA Hourly Continuation — ZEC/USDT P8_34

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1369 |
| net_profit_factor | 0.4474 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8557 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -6.7759 |
| sortino_ratio | -3.5226 |
| max_drawdown | 0.9863 |
| cagr | -0.8179 |
| net_avg_win | 12.3017 |
| net_avg_loss | -24.7847 |
| avg_hold_time_bars | 5.2863 |
| exposure | 0.3290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
