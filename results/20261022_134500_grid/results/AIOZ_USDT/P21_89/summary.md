# EMA Hourly Continuation — AIOZ/USDT P21_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.6510 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9270 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -4.5424 |
| sortino_ratio | -1.7505 |
| max_drawdown | 0.8823 |
| cagr | -0.5692 |
| net_avg_win | 46.7273 |
| net_avg_loss | -62.8288 |
| avg_hold_time_bars | 11.2207 |
| exposure | 0.3835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
