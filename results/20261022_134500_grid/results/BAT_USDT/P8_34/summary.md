# EMA Hourly Continuation — BAT/USDT P8_34

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1318 |
| net_profit_factor | 0.4184 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -8.1429 |
| sortino_ratio | -4.1534 |
| max_drawdown | 0.9941 |
| cagr | -0.8697 |
| net_avg_win | 11.9796 |
| net_avg_loss | -23.7058 |
| avg_hold_time_bars | 5.8900 |
| exposure | 0.3529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
