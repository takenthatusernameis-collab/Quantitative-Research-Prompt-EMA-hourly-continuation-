# EMA Hourly Continuation — CSPR/USDT P144_200

**Symbol:** CSPR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.3572 |
| net_win_rate | 0.3720 |
| gross_profit_factor | 0.6954 |
| gross_win_rate | 0.3907 |
| sharpe_ratio | -7.3644 |
| sortino_ratio | -2.4246 |
| max_drawdown | 0.9524 |
| cagr | -0.6999 |
| net_avg_win | 26.5693 |
| net_avg_loss | -44.0489 |
| avg_hold_time_bars | 4.2000 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
