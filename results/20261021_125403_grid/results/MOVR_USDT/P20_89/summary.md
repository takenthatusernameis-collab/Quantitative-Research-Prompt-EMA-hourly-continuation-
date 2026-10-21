# EMA Hourly Continuation — MOVR/USDT P20_89

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.6867 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -2.8694 |
| sortino_ratio | -0.9702 |
| max_drawdown | 0.6931 |
| cagr | -0.3601 |
| net_avg_win | 56.8182 |
| net_avg_loss | -70.0779 |
| avg_hold_time_bars | 13.7760 |
| exposure | 0.3550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
