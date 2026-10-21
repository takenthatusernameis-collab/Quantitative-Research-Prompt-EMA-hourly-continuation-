# EMA Hourly Continuation — RIO/USDT P100_144

**Symbol:** RIO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.7275 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -1.3969 |
| sortino_ratio | -0.2821 |
| max_drawdown | 0.2950 |
| cagr | -0.1218 |
| net_avg_win | 79.2462 |
| net_avg_loss | -94.6723 |
| avg_hold_time_bars | 6.3800 |
| exposure | 0.0586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
