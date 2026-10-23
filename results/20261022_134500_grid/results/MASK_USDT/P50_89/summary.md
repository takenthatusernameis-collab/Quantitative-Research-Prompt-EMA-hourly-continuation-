# EMA Hourly Continuation — MASK/USDT P50_89

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.3768 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.7806 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -7.6714 |
| sortino_ratio | -2.8924 |
| max_drawdown | 0.9761 |
| cagr | -0.7704 |
| net_avg_win | 19.2064 |
| net_avg_loss | -38.4472 |
| avg_hold_time_bars | 4.7997 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
