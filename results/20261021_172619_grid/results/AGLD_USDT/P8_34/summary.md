# EMA Hourly Continuation — AGLD/USDT P8_34

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -3.1272 |
| sortino_ratio | -1.2725 |
| max_drawdown | 0.7756 |
| cagr | -0.4411 |
| net_avg_win | 46.7173 |
| net_avg_loss | -62.1476 |
| avg_hold_time_bars | 8.6474 |
| exposure | 0.3186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
