# EMA Hourly Continuation — AAVE/USDT P26_34

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.2496 |
| net_win_rate | 0.3638 |
| gross_profit_factor | 0.6980 |
| gross_win_rate | 0.3934 |
| sharpe_ratio | -13.5342 |
| sortino_ratio | -6.4847 |
| max_drawdown | 0.9998 |
| cagr | -0.9679 |
| net_avg_win | 8.4420 |
| net_avg_loss | -19.3387 |
| avg_hold_time_bars | 1.9058 |
| exposure | 0.0938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
