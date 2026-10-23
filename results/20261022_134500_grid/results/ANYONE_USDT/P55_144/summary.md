# EMA Hourly Continuation — ANYONE/USDT P55_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.7884 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -3.1935 |
| sortino_ratio | -0.9814 |
| max_drawdown | 0.6654 |
| cagr | -0.3684 |
| net_avg_win | 49.3329 |
| net_avg_loss | -68.8775 |
| avg_hold_time_bars | 11.1412 |
| exposure | 0.2393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
