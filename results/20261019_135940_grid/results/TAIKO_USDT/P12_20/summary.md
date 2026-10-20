# EMA Hourly Continuation — TAIKO/USDT P12_20

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1336 |
| net_profit_factor | 0.4192 |
| net_win_rate | 0.4034 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -13.2995 |
| sortino_ratio | -7.0951 |
| max_drawdown | 0.9999 |
| cagr | -0.9772 |
| net_avg_win | 13.3896 |
| net_avg_loss | -21.6007 |
| avg_hold_time_bars | 2.5734 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
