# EMA Hourly Continuation — SHR/USDT P89_200

**Symbol:** SHR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.4955 |
| net_win_rate | 0.3756 |
| gross_profit_factor | 0.6731 |
| gross_win_rate | 0.3756 |
| sharpe_ratio | -5.9480 |
| sortino_ratio | -2.0007 |
| max_drawdown | 0.9177 |
| cagr | -0.6204 |
| net_avg_win | 40.9527 |
| net_avg_loss | -49.7250 |
| avg_hold_time_bars | 8.0943 |
| exposure | 0.2135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
