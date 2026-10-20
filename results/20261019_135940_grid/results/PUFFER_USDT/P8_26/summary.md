# EMA Hourly Continuation — PUFFER/USDT P8_26

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.9133 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -7.2200 |
| sortino_ratio | -3.7207 |
| max_drawdown | 0.9756 |
| cagr | -0.8390 |
| net_avg_win | 25.2583 |
| net_avg_loss | -37.9713 |
| avg_hold_time_bars | 4.8808 |
| exposure | 0.3013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
