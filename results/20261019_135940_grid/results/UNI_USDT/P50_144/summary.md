# EMA Hourly Continuation — UNI/USDT P50_144

**Symbol:** UNI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6052 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.4705 |
| sortino_ratio | -1.0720 |
| max_drawdown | 0.7389 |
| cagr | -0.4036 |
| net_avg_win | 48.0194 |
| net_avg_loss | -74.5321 |
| avg_hold_time_bars | 13.3758 |
| exposure | 0.2912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
