# EMA Hourly Continuation — BOME/USDT P20_50

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.4579 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.7503 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -6.3934 |
| sortino_ratio | -2.7927 |
| max_drawdown | 0.9710 |
| cagr | -0.7427 |
| net_avg_win | 18.8613 |
| net_avg_loss | -33.3387 |
| avg_hold_time_bars | 4.8285 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
