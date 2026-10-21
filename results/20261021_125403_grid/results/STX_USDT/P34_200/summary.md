# EMA Hourly Continuation — STX/USDT P34_200

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.9599 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1479 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.1597 |
| sortino_ratio | -0.0389 |
| max_drawdown | 0.2008 |
| cagr | -0.0223 |
| net_avg_win | 86.1356 |
| net_avg_loss | -104.6849 |
| avg_hold_time_bars | 39.9126 |
| exposure | 0.5165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
