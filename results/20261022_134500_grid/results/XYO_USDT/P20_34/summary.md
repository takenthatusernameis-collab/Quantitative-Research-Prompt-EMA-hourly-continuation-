# EMA Hourly Continuation — XYO/USDT P20_34

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1225 |
| net_profit_factor | 0.2684 |
| net_win_rate | 0.3567 |
| gross_profit_factor | 0.6693 |
| gross_win_rate | 0.3861 |
| sharpe_ratio | -13.7283 |
| sortino_ratio | -6.9278 |
| max_drawdown | 0.9999 |
| cagr | -0.9712 |
| net_avg_win | 8.3947 |
| net_avg_loss | -17.3441 |
| avg_hold_time_bars | 3.2008 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
