# EMA Hourly Continuation — CARV/USDT P89_144

**Symbol:** CARV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.4837 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8622 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -4.4549 |
| sortino_ratio | -1.3267 |
| max_drawdown | 0.7264 |
| cagr | -0.4684 |
| net_avg_win | 41.5174 |
| net_avg_loss | -71.0239 |
| avg_hold_time_bars | 6.0889 |
| exposure | 0.1234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
