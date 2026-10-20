# EMA Hourly Continuation — OGN/USDT P21_144

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5807 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -4.4452 |
| sortino_ratio | -1.3803 |
| max_drawdown | 0.8261 |
| cagr | -0.4869 |
| net_avg_win | 52.6920 |
| net_avg_loss | -68.8589 |
| avg_hold_time_bars | 24.8226 |
| exposure | 0.5571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
