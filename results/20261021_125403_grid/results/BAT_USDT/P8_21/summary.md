# EMA Hourly Continuation — BAT/USDT P8_21

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.6562 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 1.0079 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -4.1015 |
| sortino_ratio | -1.6003 |
| max_drawdown | 0.8443 |
| cagr | -0.5195 |
| net_avg_win | 44.7252 |
| net_avg_loss | -64.2234 |
| avg_hold_time_bars | 5.4932 |
| exposure | 0.1848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
