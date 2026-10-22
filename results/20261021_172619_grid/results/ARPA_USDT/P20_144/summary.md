# EMA Hourly Continuation — ARPA/USDT P20_144

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6779 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8699 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -2.6732 |
| sortino_ratio | -0.8207 |
| max_drawdown | 0.6393 |
| cagr | -0.3147 |
| net_avg_win | 59.3310 |
| net_avg_loss | -76.3197 |
| avg_hold_time_bars | 24.5748 |
| exposure | 0.5204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
