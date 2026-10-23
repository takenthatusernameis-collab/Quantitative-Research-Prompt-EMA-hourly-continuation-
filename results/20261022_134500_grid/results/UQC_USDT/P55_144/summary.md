# EMA Hourly Continuation — UQC/USDT P55_144

**Symbol:** UQC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.1897 |
| net_win_rate | 0.2759 |
| gross_profit_factor | 0.4004 |
| gross_win_rate | 0.2862 |
| sharpe_ratio | -7.1812 |
| sortino_ratio | -1.7198 |
| max_drawdown | 0.9004 |
| cagr | -0.5992 |
| net_avg_win | 26.3448 |
| net_avg_loss | -52.9109 |
| avg_hold_time_bars | 37.7379 |
| exposure | 0.4953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
