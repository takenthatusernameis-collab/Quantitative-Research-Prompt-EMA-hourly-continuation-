# EMA Hourly Continuation — SUI/USDT P55_89

**Symbol:** SUI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5261 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9556 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -5.5363 |
| sortino_ratio | -2.0641 |
| max_drawdown | 0.9216 |
| cagr | -0.6328 |
| net_avg_win | 31.1170 |
| net_avg_loss | -53.0016 |
| avg_hold_time_bars | 3.5086 |
| exposure | 0.1107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
