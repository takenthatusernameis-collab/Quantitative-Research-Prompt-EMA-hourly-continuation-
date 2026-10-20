# EMA Hourly Continuation — CKB/USDT P26_55

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.5090 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -7.6885 |
| sortino_ratio | -3.3141 |
| max_drawdown | 0.9835 |
| cagr | -0.8005 |
| net_avg_win | 25.2738 |
| net_avg_loss | -38.1883 |
| avg_hold_time_bars | 4.3301 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
