# EMA Hourly Continuation — UQC/USDT P26_200

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.3681 |
| net_win_rate | 0.3095 |
| gross_profit_factor | 0.4522 |
| gross_win_rate | 0.3095 |
| sharpe_ratio | -3.9230 |
| sortino_ratio | -0.7045 |
| max_drawdown | 0.5721 |
| cagr | -0.2858 |
| net_avg_win | 64.0819 |
| net_avg_loss | -78.0438 |
| avg_hold_time_bars | 93.0298 |
| exposure | 0.7074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
