# EMA Hourly Continuation — FIL/USDT P26_34

**Symbol:** FIL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.7006 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9872 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.3686 |
| sortino_ratio | -0.2415 |
| max_drawdown | 0.2697 |
| cagr | -0.1045 |
| net_avg_win | 75.5424 |
| net_avg_loss | -106.4070 |
| avg_hold_time_bars | 4.8808 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
