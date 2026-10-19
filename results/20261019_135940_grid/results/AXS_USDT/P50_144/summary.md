# EMA Hourly Continuation — AXS/USDT P50_144

**Symbol:** AXS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0572 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -2.3610 |
| sortino_ratio | -0.7043 |
| max_drawdown | 0.6008 |
| cagr | -0.2819 |
| net_avg_win | 59.4716 |
| net_avg_loss | -87.3589 |
| avg_hold_time_bars | 13.7517 |
| exposure | 0.2757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
