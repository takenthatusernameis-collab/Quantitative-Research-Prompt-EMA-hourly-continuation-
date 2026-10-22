# EMA Hourly Continuation — DASH/USDT P34_200

**Symbol:** DASH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.5035 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8454 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.9473 |
| sortino_ratio | -1.1256 |
| max_drawdown | 0.7775 |
| cagr | -0.4266 |
| net_avg_win | 40.1633 |
| net_avg_loss | -66.4775 |
| avg_hold_time_bars | 26.0981 |
| exposure | 0.4959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
