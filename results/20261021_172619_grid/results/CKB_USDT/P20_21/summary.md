# EMA Hourly Continuation — CKB/USDT P20_21

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.4445 |
| net_win_rate | 0.3902 |
| gross_profit_factor | 0.6467 |
| gross_win_rate | 0.3902 |
| sharpe_ratio | -3.2582 |
| sortino_ratio | -0.5956 |
| max_drawdown | 0.5121 |
| cagr | -0.2419 |
| net_avg_win | 62.6455 |
| net_avg_loss | -90.2055 |
| avg_hold_time_bars | 4.4878 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
