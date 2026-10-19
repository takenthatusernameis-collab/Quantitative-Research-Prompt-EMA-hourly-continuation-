# EMA Hourly Continuation — AR/USDT P8_100

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9053 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -2.9591 |
| sortino_ratio | -0.9818 |
| max_drawdown | 0.7024 |
| cagr | -0.3743 |
| net_avg_win | 50.0426 |
| net_avg_loss | -69.3494 |
| avg_hold_time_bars | 28.4442 |
| exposure | 0.7189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
