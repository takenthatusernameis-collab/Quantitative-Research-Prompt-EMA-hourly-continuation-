# EMA Hourly Continuation — ZBCN/USDT P89_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.4904 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8038 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -4.9942 |
| sortino_ratio | -1.6968 |
| max_drawdown | 0.8739 |
| cagr | -0.5638 |
| net_avg_win | 32.4791 |
| net_avg_loss | -53.7369 |
| avg_hold_time_bars | 4.1441 |
| exposure | 0.1104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
