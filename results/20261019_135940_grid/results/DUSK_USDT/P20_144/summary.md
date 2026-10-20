# EMA Hourly Continuation — DUSK/USDT P20_144

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6607 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9095 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.6869 |
| sortino_ratio | -0.8307 |
| max_drawdown | 0.6484 |
| cagr | -0.3231 |
| net_avg_win | 53.5923 |
| net_avg_loss | -72.4893 |
| avg_hold_time_bars | 24.3077 |
| exposure | 0.5315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
