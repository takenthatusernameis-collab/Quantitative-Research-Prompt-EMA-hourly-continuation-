# EMA Hourly Continuation — ZEC/USDT P12_34

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1276 |
| net_profit_factor | 0.4176 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -6.9404 |
| sortino_ratio | -3.4892 |
| max_drawdown | 0.9863 |
| cagr | -0.8180 |
| net_avg_win | 11.5920 |
| net_avg_loss | -25.4241 |
| avg_hold_time_bars | 3.8636 |
| exposure | 0.2241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
