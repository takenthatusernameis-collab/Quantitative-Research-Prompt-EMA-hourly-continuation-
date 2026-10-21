# EMA Hourly Continuation — EDU/USDT P12_50

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.5431 |
| sortino_ratio | -0.9868 |
| max_drawdown | 0.6861 |
| cagr | -0.3654 |
| net_avg_win | 49.8441 |
| net_avg_loss | -65.3133 |
| avg_hold_time_bars | 9.6478 |
| exposure | 0.3235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
