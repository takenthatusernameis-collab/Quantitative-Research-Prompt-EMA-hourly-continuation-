# EMA Hourly Continuation — ETHFI/USDT P21_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.8987 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -0.6162 |
| sortino_ratio | -0.1506 |
| max_drawdown | 0.2869 |
| cagr | -0.0696 |
| net_avg_win | 100.0173 |
| net_avg_loss | -113.6146 |
| avg_hold_time_bars | 48.1890 |
| exposure | 0.6374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
