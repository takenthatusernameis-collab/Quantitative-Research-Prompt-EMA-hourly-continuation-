# EMA Hourly Continuation — ORBS/USDT P12_20

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1434 |
| net_profit_factor | 0.2041 |
| net_win_rate | 0.3326 |
| gross_profit_factor | 0.7266 |
| gross_win_rate | 0.3919 |
| sharpe_ratio | -16.7057 |
| sortino_ratio | -9.2407 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 5.3747 |
| net_avg_loss | -13.1282 |
| avg_hold_time_bars | 3.6360 |
| exposure | 0.2370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
