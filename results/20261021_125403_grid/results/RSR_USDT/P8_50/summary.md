# EMA Hourly Continuation — RSR/USDT P8_50

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.7930 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.0217 |
| sortino_ratio | -0.7693 |
| max_drawdown | 0.6170 |
| cagr | -0.2993 |
| net_avg_win | 65.1997 |
| net_avg_loss | -78.8146 |
| avg_hold_time_bars | 13.2948 |
| exposure | 0.4285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
