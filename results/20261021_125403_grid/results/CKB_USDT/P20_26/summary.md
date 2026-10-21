# EMA Hourly Continuation — CKB/USDT P20_26

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.4891 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.7116 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -3.3159 |
| sortino_ratio | -0.6808 |
| max_drawdown | 0.5651 |
| cagr | -0.2695 |
| net_avg_win | 61.4387 |
| net_avg_loss | -87.5220 |
| avg_hold_time_bars | 4.7923 |
| exposure | 0.0451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
