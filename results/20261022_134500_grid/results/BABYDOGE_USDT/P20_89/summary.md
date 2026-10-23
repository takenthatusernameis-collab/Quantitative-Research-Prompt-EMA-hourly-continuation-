# EMA Hourly Continuation — BABYDOGE/USDT P20_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 52 |
| net_profit_factor | 0.9990 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0695 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | 0.0205 |
| sortino_ratio | 0.0021 |
| max_drawdown | 0.0622 |
| cagr | -0.0001 |
| net_avg_win | 94.4287 |
| net_avg_loss | -102.0836 |
| avg_hold_time_bars | 61.9038 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
