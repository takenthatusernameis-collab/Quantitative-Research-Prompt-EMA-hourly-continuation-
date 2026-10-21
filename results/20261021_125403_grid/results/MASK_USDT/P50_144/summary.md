# EMA Hourly Continuation — MASK/USDT P50_144

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7141 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0203 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.9028 |
| sortino_ratio | -0.5328 |
| max_drawdown | 0.4798 |
| cagr | -0.2211 |
| net_avg_win | 58.7906 |
| net_avg_loss | -85.7969 |
| avg_hold_time_bars | 14.5670 |
| exposure | 0.2569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
