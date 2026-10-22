# EMA Hourly Continuation — ARB/USDT P12_26

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1357 |
| net_profit_factor | 0.3569 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -9.8775 |
| sortino_ratio | -5.1642 |
| max_drawdown | 0.9984 |
| cagr | -0.9218 |
| net_avg_win | 9.0242 |
| net_avg_loss | -20.8940 |
| avg_hold_time_bars | 2.8091 |
| exposure | 0.1733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
