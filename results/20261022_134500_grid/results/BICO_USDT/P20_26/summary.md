# EMA Hourly Continuation — BICO/USDT P20_26

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1089 |
| net_profit_factor | 0.2907 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.7827 |
| gross_win_rate | 0.4362 |
| sharpe_ratio | -11.2706 |
| sortino_ratio | -5.3223 |
| max_drawdown | 0.9988 |
| cagr | -0.9309 |
| net_avg_win | 9.5211 |
| net_avg_loss | -21.3686 |
| avg_hold_time_bars | 2.7117 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
