# EMA Hourly Continuation — PYTH/USDT P12_34

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1280 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -7.6900 |
| sortino_ratio | -3.8553 |
| max_drawdown | 0.9919 |
| cagr | -0.8502 |
| net_avg_win | 18.7003 |
| net_avg_loss | -30.0769 |
| avg_hold_time_bars | 3.8070 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
