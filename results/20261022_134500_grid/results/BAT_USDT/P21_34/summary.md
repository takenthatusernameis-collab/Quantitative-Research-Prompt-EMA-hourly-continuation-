# EMA Hourly Continuation — BAT/USDT P21_34

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.2788 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.7922 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -10.6560 |
| sortino_ratio | -5.1320 |
| max_drawdown | 0.9983 |
| cagr | -0.9215 |
| net_avg_win | 8.2304 |
| net_avg_loss | -20.9747 |
| avg_hold_time_bars | 2.9858 |
| exposure | 0.1532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
