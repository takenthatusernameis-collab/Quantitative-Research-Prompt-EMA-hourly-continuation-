# EMA Hourly Continuation — GMEE/USDT P26_200

**Symbol:** GMEE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5662 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.7374 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -3.4002 |
| sortino_ratio | -0.9418 |
| max_drawdown | 0.6857 |
| cagr | -0.3616 |
| net_avg_win | 52.2193 |
| net_avg_loss | -69.5781 |
| avg_hold_time_bars | 31.5420 |
| exposure | 0.5635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
