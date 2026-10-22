# EMA Hourly Continuation — ILV/USDT P26_55

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7383 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2229 |
| sortino_ratio | -0.7019 |
| max_drawdown | 0.5860 |
| cagr | -0.2739 |
| net_avg_win | 64.3769 |
| net_avg_loss | -87.2002 |
| avg_hold_time_bars | 6.3079 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
