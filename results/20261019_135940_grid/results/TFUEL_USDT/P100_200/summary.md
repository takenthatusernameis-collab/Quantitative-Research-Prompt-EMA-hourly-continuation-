# EMA Hourly Continuation — TFUEL/USDT P100_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.4296 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.7627 |
| gross_win_rate | 0.4012 |
| sharpe_ratio | -6.8648 |
| sortino_ratio | -2.2138 |
| max_drawdown | 0.9395 |
| cagr | -0.6686 |
| net_avg_win | 34.6402 |
| net_avg_loss | -51.8926 |
| avg_hold_time_bars | 7.3321 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
