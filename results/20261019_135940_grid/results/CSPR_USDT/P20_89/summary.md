# EMA Hourly Continuation — CSPR/USDT P20_89

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.4486 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.7859 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -7.7362 |
| sortino_ratio | -3.4303 |
| max_drawdown | 0.9861 |
| cagr | -0.8139 |
| net_avg_win | 19.3636 |
| net_avg_loss | -30.5469 |
| avg_hold_time_bars | 8.0651 |
| exposure | 0.3662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
