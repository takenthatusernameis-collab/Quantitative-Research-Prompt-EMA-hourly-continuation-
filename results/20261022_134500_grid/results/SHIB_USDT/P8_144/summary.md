# EMA Hourly Continuation — SHIB/USDT P8_144

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0731 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -3.3049 |
| sortino_ratio | -1.1002 |
| max_drawdown | 0.7483 |
| cagr | -0.4142 |
| net_avg_win | 52.6964 |
| net_avg_loss | -78.1569 |
| avg_hold_time_bars | 27.6584 |
| exposure | 0.7103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
