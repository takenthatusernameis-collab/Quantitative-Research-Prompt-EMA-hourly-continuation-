# EMA Hourly Continuation — ALEX/USDT P12_55

**Symbol:** ALEX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 872 |
| net_profit_factor | 0.5926 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -6.6846 |
| sortino_ratio | -2.7567 |
| max_drawdown | 0.9707 |
| cagr | -0.7466 |
| net_avg_win | 37.8611 |
| net_avg_loss | -47.5323 |
| avg_hold_time_bars | 10.3131 |
| exposure | 0.4088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
