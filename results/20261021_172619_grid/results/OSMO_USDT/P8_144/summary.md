# EMA Hourly Continuation — OSMO/USDT P8_144

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8652 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -0.9482 |
| sortino_ratio | -0.2709 |
| max_drawdown | 0.3883 |
| cagr | -0.1199 |
| net_avg_win | 86.7523 |
| net_avg_loss | -104.9212 |
| avg_hold_time_bars | 40.5214 |
| exposure | 0.7312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
