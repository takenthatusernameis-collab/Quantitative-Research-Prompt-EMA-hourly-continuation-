# EMA Hourly Continuation — COTI/USDT P50_55

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 845 |
| net_profit_factor | 0.2214 |
| net_win_rate | 0.3680 |
| gross_profit_factor | 0.6081 |
| gross_win_rate | 0.4059 |
| sharpe_ratio | -11.9168 |
| sortino_ratio | -5.0535 |
| max_drawdown | 0.9989 |
| cagr | -0.9325 |
| net_avg_win | 9.1350 |
| net_avg_loss | -24.0252 |
| avg_hold_time_bars | 1.7456 |
| exposure | 0.0670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
