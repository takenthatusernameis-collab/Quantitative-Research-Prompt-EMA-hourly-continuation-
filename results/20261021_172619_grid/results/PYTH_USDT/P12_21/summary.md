# EMA Hourly Continuation — PYTH/USDT P12_21

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8113 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0868 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.1610 |
| sortino_ratio | -0.2930 |
| max_drawdown | 0.3535 |
| cagr | -0.1264 |
| net_avg_win | 77.3179 |
| net_avg_loss | -103.7252 |
| avg_hold_time_bars | 4.7264 |
| exposure | 0.0660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
