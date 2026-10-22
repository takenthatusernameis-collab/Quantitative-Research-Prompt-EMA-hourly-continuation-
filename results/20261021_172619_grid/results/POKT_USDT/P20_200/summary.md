# EMA Hourly Continuation — POKT/USDT P20_200

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.6943 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -2.7029 |
| sortino_ratio | -0.7478 |
| max_drawdown | 0.6218 |
| cagr | -0.2922 |
| net_avg_win | 78.1740 |
| net_avg_loss | -87.6934 |
| avg_hold_time_bars | 35.7332 |
| exposure | 0.6242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
