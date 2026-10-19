# EMA Hourly Continuation — XDC/USDT P50_55

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.0628 |
| net_win_rate | 0.2891 |
| gross_profit_factor | 0.3813 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -15.4034 |
| sortino_ratio | -7.0073 |
| max_drawdown | 1.0000 |
| cagr | -0.9810 |
| net_avg_win | 2.7479 |
| net_avg_loss | -17.7834 |
| avg_hold_time_bars | 2.0403 |
| exposure | 0.0783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
