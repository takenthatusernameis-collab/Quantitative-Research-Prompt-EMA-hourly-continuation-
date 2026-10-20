# EMA Hourly Continuation — MOVR/USDT P20_21

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1284 |
| net_profit_factor | 0.1481 |
| net_win_rate | 0.2952 |
| gross_profit_factor | 0.6175 |
| gross_win_rate | 0.3894 |
| sharpe_ratio | -17.7154 |
| sortino_ratio | -9.5171 |
| max_drawdown | 1.0000 |
| cagr | -0.9950 |
| net_avg_win | 4.5868 |
| net_avg_loss | -12.9706 |
| avg_hold_time_bars | 1.9058 |
| exposure | 0.1112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
