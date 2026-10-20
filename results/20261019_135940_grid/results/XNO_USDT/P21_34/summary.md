# EMA Hourly Continuation — XNO/USDT P21_34

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1268 |
| net_profit_factor | 0.3307 |
| net_win_rate | 0.3683 |
| gross_profit_factor | 0.8127 |
| gross_win_rate | 0.3951 |
| sharpe_ratio | -13.2283 |
| sortino_ratio | -6.7626 |
| max_drawdown | 0.9998 |
| cagr | -0.9678 |
| net_avg_win | 10.5772 |
| net_avg_loss | -18.6489 |
| avg_hold_time_bars | 2.4771 |
| exposure | 0.1428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
