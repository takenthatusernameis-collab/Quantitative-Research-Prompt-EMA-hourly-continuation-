# EMA Hourly Continuation — QNT/USDT P8_200

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7343 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0480 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -2.0907 |
| sortino_ratio | -0.6780 |
| max_drawdown | 0.5868 |
| cagr | -0.2719 |
| net_avg_win | 57.0564 |
| net_avg_loss | -81.3770 |
| avg_hold_time_bars | 31.3750 |
| exposure | 0.7416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
