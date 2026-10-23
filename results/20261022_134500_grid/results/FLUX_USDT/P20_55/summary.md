# EMA Hourly Continuation — FLUX/USDT P20_55

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.5361 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -6.4611 |
| sortino_ratio | -2.8422 |
| max_drawdown | 0.9706 |
| cagr | -0.7542 |
| net_avg_win | 24.4315 |
| net_avg_loss | -39.5446 |
| avg_hold_time_bars | 4.7966 |
| exposure | 0.2154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
