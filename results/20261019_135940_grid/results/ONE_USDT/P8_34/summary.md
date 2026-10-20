# EMA Hourly Continuation — ONE/USDT P8_34

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1431 |
| net_profit_factor | 0.5060 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -8.4511 |
| sortino_ratio | -4.4828 |
| max_drawdown | 0.9963 |
| cagr | -0.8891 |
| net_avg_win | 15.8446 |
| net_avg_loss | -25.6213 |
| avg_hold_time_bars | 5.1635 |
| exposure | 0.3359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
