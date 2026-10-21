# EMA Hourly Continuation — KAVA/USDT P12_20

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.2291 |
| sortino_ratio | -1.2559 |
| max_drawdown | 0.7753 |
| cagr | -0.4437 |
| net_avg_win | 53.0084 |
| net_avg_loss | -78.5704 |
| avg_hold_time_bars | 6.0070 |
| exposure | 0.1169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
