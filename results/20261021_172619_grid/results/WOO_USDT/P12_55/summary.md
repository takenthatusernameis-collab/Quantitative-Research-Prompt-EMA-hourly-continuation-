# EMA Hourly Continuation — WOO/USDT P12_55

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.4116 |
| sortino_ratio | -0.8827 |
| max_drawdown | 0.6734 |
| cagr | -0.3344 |
| net_avg_win | 71.2840 |
| net_avg_loss | -86.2182 |
| avg_hold_time_bars | 12.7823 |
| exposure | 0.3817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
