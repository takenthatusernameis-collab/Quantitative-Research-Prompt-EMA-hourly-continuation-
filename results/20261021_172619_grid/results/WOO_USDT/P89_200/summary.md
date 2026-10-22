# EMA Hourly Continuation — WOO/USDT P89_200

**Symbol:** WOO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -1.4948 |
| sortino_ratio | -0.3570 |
| max_drawdown | 0.3514 |
| cagr | -0.1512 |
| net_avg_win | 74.6883 |
| net_avg_loss | -95.8240 |
| avg_hold_time_bars | 14.4301 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
