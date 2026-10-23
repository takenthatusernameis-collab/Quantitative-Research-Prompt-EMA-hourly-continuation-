# EMA Hourly Continuation — MANTA/USDT P21_200

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.8555 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.1406 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.8703 |
| sortino_ratio | -0.2104 |
| max_drawdown | 0.3332 |
| cagr | -0.0952 |
| net_avg_win | 87.0819 |
| net_avg_loss | -111.3829 |
| avg_hold_time_bars | 52.1661 |
| exposure | 0.6853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
