# EMA Hourly Continuation — NOT/USDT P26_34

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1081 |
| net_profit_factor | 0.3733 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.7660 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -11.6942 |
| sortino_ratio | -5.5826 |
| max_drawdown | 0.9992 |
| cagr | -0.9459 |
| net_avg_win | 13.7163 |
| net_avg_loss | -24.6437 |
| avg_hold_time_bars | 1.8788 |
| exposure | 0.0954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
