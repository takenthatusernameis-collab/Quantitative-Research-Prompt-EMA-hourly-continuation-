# EMA Hourly Continuation — UNI/USDT P50_55

**Symbol:** UNI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.1763 |
| net_win_rate | 0.3141 |
| gross_profit_factor | 0.6326 |
| gross_win_rate | 0.3661 |
| sharpe_ratio | -14.0420 |
| sortino_ratio | -6.1719 |
| max_drawdown | 0.9998 |
| cagr | -0.9677 |
| net_avg_win | 7.8670 |
| net_avg_loss | -20.4344 |
| avg_hold_time_bars | 1.7633 |
| exposure | 0.0694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
