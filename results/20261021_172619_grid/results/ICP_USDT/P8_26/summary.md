# EMA Hourly Continuation — ICP/USDT P8_26

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.7719 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0475 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -2.0587 |
| sortino_ratio | -0.7440 |
| max_drawdown | 0.6194 |
| cagr | -0.2895 |
| net_avg_win | 60.3475 |
| net_avg_loss | -81.9922 |
| avg_hold_time_bars | 6.0681 |
| exposure | 0.1740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
