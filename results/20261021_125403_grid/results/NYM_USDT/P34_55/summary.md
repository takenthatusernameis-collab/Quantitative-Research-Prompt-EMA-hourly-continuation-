# EMA Hourly Continuation — NYM/USDT P34_55

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.4095 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.7028 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -4.0850 |
| sortino_ratio | -0.9547 |
| max_drawdown | 0.6769 |
| cagr | -0.3589 |
| net_avg_win | 42.0142 |
| net_avg_loss | -73.4809 |
| avg_hold_time_bars | 11.5038 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
