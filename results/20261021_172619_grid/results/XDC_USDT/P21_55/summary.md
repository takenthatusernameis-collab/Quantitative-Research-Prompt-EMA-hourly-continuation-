# EMA Hourly Continuation — XDC/USDT P21_55

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.5643 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -3.4268 |
| sortino_ratio | -1.0156 |
| max_drawdown | 0.6907 |
| cagr | -0.3719 |
| net_avg_win | 43.9564 |
| net_avg_loss | -70.2779 |
| avg_hold_time_bars | 9.0117 |
| exposure | 0.1753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
