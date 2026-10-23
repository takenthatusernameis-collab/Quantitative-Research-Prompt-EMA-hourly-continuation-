# EMA Hourly Continuation — POKT/USDT P21_100

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.6003 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.8933 |
| gross_win_rate | 0.4232 |
| sharpe_ratio | -6.3714 |
| sortino_ratio | -2.6095 |
| max_drawdown | 0.9585 |
| cagr | -0.7126 |
| net_avg_win | 40.3669 |
| net_avg_loss | -48.1694 |
| avg_hold_time_bars | 10.5369 |
| exposure | 0.4067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
