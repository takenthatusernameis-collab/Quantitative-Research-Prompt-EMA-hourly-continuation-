# EMA Hourly Continuation — FIL/USDT P8_200

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9783 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.8639 |
| sortino_ratio | -0.4443 |
| max_drawdown | 0.4591 |
| cagr | -0.1942 |
| net_avg_win | 68.8876 |
| net_avg_loss | -96.4203 |
| avg_hold_time_bars | 63.2740 |
| exposure | 0.8398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
