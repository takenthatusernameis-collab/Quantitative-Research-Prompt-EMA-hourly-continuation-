# EMA Hourly Continuation — TRAC/USDT P100_144

**Symbol:** TRAC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -4.5185 |
| sortino_ratio | -1.4495 |
| max_drawdown | 0.8321 |
| cagr | -0.5040 |
| net_avg_win | 32.7236 |
| net_avg_loss | -61.4098 |
| avg_hold_time_bars | 3.9922 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
