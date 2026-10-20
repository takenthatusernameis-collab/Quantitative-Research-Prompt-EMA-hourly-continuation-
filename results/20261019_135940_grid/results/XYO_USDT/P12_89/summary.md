# EMA Hourly Continuation — XYO/USDT P12_89

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.4601 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.7606 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -7.7715 |
| sortino_ratio | -3.3053 |
| max_drawdown | 0.9843 |
| cagr | -0.8045 |
| net_avg_win | 21.8880 |
| net_avg_loss | -33.5548 |
| avg_hold_time_bars | 11.6242 |
| exposure | 0.4871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
