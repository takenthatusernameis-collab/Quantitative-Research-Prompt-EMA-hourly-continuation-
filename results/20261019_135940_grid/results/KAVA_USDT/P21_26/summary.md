# EMA Hourly Continuation — KAVA/USDT P21_26

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.1868 |
| net_win_rate | 0.3143 |
| gross_profit_factor | 0.7736 |
| gross_win_rate | 0.4046 |
| sharpe_ratio | -17.1028 |
| sortino_ratio | -9.1259 |
| max_drawdown | 1.0000 |
| cagr | -0.9929 |
| net_avg_win | 5.7870 |
| net_avg_loss | -14.2002 |
| avg_hold_time_bars | 2.5012 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
