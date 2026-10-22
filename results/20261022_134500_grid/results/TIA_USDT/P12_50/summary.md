# EMA Hourly Continuation — TIA/USDT P12_50

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9493 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -5.5543 |
| sortino_ratio | -2.5688 |
| max_drawdown | 0.9544 |
| cagr | -0.7065 |
| net_avg_win | 31.9284 |
| net_avg_loss | -45.0008 |
| avg_hold_time_bars | 6.8737 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
