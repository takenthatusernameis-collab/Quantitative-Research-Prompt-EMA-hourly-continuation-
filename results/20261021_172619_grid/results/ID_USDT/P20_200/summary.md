# EMA Hourly Continuation — ID/USDT P20_200

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.9220 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1059 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -0.3958 |
| sortino_ratio | -0.0990 |
| max_drawdown | 0.1606 |
| cagr | -0.0479 |
| net_avg_win | 86.1053 |
| net_avg_loss | -104.4926 |
| avg_hold_time_bars | 47.4884 |
| exposure | 0.6512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
