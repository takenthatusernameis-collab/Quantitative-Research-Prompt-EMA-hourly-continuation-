# EMA Hourly Continuation — SHIB/USDT P34_50

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.6541 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -2.0581 |
| sortino_ratio | -0.4260 |
| max_drawdown | 0.4572 |
| cagr | -0.1766 |
| net_avg_win | 72.3101 |
| net_avg_loss | -105.3354 |
| avg_hold_time_bars | 5.3865 |
| exposure | 0.0507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
