# EMA Hourly Continuation — SUI/USDT P89_144

**Symbol:** SUI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.4586 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.7962 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.6799 |
| sortino_ratio | -1.8291 |
| max_drawdown | 0.8950 |
| cagr | -0.5887 |
| net_avg_win | 34.2170 |
| net_avg_loss | -55.8906 |
| avg_hold_time_bars | 4.4360 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
