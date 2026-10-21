# EMA Hourly Continuation — EDU/USDT P21_34

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.5880 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8259 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -3.4684 |
| sortino_ratio | -1.0404 |
| max_drawdown | 0.7043 |
| cagr | -0.3807 |
| net_avg_win | 49.8083 |
| net_avg_loss | -70.0667 |
| avg_hold_time_bars | 5.0946 |
| exposure | 0.1024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
