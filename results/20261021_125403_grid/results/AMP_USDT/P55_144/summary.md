# EMA Hourly Continuation — AMP/USDT P55_144

**Symbol:** AMP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5269 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.6860 |
| gross_win_rate | 0.4145 |
| sharpe_ratio | -3.8981 |
| sortino_ratio | -1.1242 |
| max_drawdown | 0.7506 |
| cagr | -0.4056 |
| net_avg_win | 47.2122 |
| net_avg_loss | -63.4276 |
| avg_hold_time_bars | 13.7711 |
| exposure | 0.2598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
