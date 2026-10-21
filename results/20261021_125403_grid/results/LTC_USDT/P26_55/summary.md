# EMA Hourly Continuation — LTC/USDT P26_55

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6638 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -2.4285 |
| sortino_ratio | -0.6742 |
| max_drawdown | 0.5612 |
| cagr | -0.2643 |
| net_avg_win | 56.7250 |
| net_avg_loss | -86.3847 |
| avg_hold_time_bars | 6.4597 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
