# EMA Hourly Continuation — LUNA/USDT P21_200

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8189 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9916 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.1170 |
| sortino_ratio | -0.2863 |
| max_drawdown | 0.3077 |
| cagr | -0.1250 |
| net_avg_win | 80.4969 |
| net_avg_loss | -97.6909 |
| avg_hold_time_bars | 40.0436 |
| exposure | 0.5843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
