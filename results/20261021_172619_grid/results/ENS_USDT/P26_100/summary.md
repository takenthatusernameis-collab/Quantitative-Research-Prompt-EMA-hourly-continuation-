# EMA Hourly Continuation — ENS/USDT P26_100

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.8591 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0884 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -1.0761 |
| sortino_ratio | -0.3354 |
| max_drawdown | 0.3895 |
| cagr | -0.1453 |
| net_avg_win | 81.4173 |
| net_avg_loss | -102.7786 |
| avg_hold_time_bars | 16.5416 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
