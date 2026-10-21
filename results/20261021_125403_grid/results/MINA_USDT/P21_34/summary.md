# EMA Hourly Continuation — MINA/USDT P21_34

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.7301 |
| sortino_ratio | -0.7894 |
| max_drawdown | 0.6387 |
| cagr | -0.3036 |
| net_avg_win | 61.6334 |
| net_avg_loss | -88.0880 |
| avg_hold_time_bars | 5.4310 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
