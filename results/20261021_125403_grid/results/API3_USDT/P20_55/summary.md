# EMA Hourly Continuation — API3/USDT P20_55

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.7557 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9930 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -2.2531 |
| sortino_ratio | -0.7674 |
| max_drawdown | 0.6015 |
| cagr | -0.2976 |
| net_avg_win | 64.7452 |
| net_avg_loss | -84.4715 |
| avg_hold_time_bars | 8.2650 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
