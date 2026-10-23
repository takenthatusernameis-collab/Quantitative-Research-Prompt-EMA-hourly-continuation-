# EMA Hourly Continuation — MASK/USDT P50_55

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.1669 |
| net_win_rate | 0.3404 |
| gross_profit_factor | 0.6439 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -13.3200 |
| sortino_ratio | -5.7902 |
| max_drawdown | 0.9997 |
| cagr | -0.9580 |
| net_avg_win | 6.9273 |
| net_avg_loss | -21.4259 |
| avg_hold_time_bars | 2.1001 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
