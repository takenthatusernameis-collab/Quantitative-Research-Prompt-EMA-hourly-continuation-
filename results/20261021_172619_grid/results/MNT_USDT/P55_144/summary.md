# EMA Hourly Continuation — MNT/USDT P55_144

**Symbol:** MNT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7692 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0506 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.3447 |
| sortino_ratio | -0.3289 |
| max_drawdown | 0.3743 |
| cagr | -0.1413 |
| net_avg_win | 71.0892 |
| net_avg_loss | -97.6661 |
| avg_hold_time_bars | 19.5241 |
| exposure | 0.2574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
