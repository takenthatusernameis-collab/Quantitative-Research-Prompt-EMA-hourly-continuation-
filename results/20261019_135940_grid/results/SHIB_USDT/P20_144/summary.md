# EMA Hourly Continuation — SHIB/USDT P20_144

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6906 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -3.0566 |
| sortino_ratio | -0.9789 |
| max_drawdown | 0.6999 |
| cagr | -0.3726 |
| net_avg_win | 60.1365 |
| net_avg_loss | -86.4095 |
| avg_hold_time_bars | 21.6420 |
| exposure | 0.5056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
