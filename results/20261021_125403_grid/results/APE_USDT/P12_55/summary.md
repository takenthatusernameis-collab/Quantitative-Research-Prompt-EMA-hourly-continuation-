# EMA Hourly Continuation — APE/USDT P12_55

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.7278 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.6823 |
| sortino_ratio | -0.9483 |
| max_drawdown | 0.6703 |
| cagr | -0.3528 |
| net_avg_win | 60.6376 |
| net_avg_loss | -76.0539 |
| avg_hold_time_bars | 12.3648 |
| exposure | 0.3451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
