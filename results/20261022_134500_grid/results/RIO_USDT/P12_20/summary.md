# EMA Hourly Continuation — RIO/USDT P12_20

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1572 |
| net_profit_factor | 0.3864 |
| net_win_rate | 0.3760 |
| gross_profit_factor | 0.7100 |
| gross_win_rate | 0.3855 |
| sharpe_ratio | -13.2050 |
| sortino_ratio | -7.3814 |
| max_drawdown | 0.9999 |
| cagr | -0.9775 |
| net_avg_win | 10.6524 |
| net_avg_loss | -16.6104 |
| avg_hold_time_bars | 2.2716 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
