# EMA Hourly Continuation — ILV/USDT P20_26

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.2366 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.6683 |
| gross_win_rate | 0.4186 |
| sharpe_ratio | -13.4511 |
| sortino_ratio | -6.6846 |
| max_drawdown | 0.9998 |
| cagr | -0.9692 |
| net_avg_win | 7.0257 |
| net_avg_loss | -17.7223 |
| avg_hold_time_bars | 2.1602 |
| exposure | 0.1159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
