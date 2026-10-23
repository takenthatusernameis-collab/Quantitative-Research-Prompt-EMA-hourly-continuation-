# EMA Hourly Continuation — CARV/USDT P20_200

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6014 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8181 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -3.3659 |
| sortino_ratio | -0.9929 |
| max_drawdown | 0.6389 |
| cagr | -0.3690 |
| net_avg_win | 58.3413 |
| net_avg_loss | -78.1042 |
| avg_hold_time_bars | 29.8153 |
| exposure | 0.5906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
