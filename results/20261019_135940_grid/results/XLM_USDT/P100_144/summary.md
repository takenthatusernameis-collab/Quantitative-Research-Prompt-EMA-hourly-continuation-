# EMA Hourly Continuation — XLM/USDT P100_144

**Symbol:** XLM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.2637 |
| net_win_rate | 0.4100 |
| gross_profit_factor | 0.7031 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -7.2600 |
| sortino_ratio | -2.2722 |
| max_drawdown | 0.9467 |
| cagr | -0.6878 |
| net_avg_win | 17.2893 |
| net_avg_loss | -45.5710 |
| avg_hold_time_bars | 3.8766 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
