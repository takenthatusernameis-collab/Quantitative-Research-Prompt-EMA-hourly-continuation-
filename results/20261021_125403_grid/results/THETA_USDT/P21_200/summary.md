# EMA Hourly Continuation — THETA/USDT P21_200

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8472 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0100 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -0.8872 |
| sortino_ratio | -0.2230 |
| max_drawdown | 0.3143 |
| cagr | -0.0992 |
| net_avg_win | 82.5355 |
| net_avg_loss | -98.6944 |
| avg_hold_time_bars | 42.0747 |
| exposure | 0.5890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
