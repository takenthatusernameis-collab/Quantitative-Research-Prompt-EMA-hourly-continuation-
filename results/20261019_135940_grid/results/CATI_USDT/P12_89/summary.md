# EMA Hourly Continuation — CATI/USDT P12_89

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.5605 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8634 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -6.0922 |
| sortino_ratio | -2.3666 |
| max_drawdown | 0.9178 |
| cagr | -0.6875 |
| net_avg_win | 42.1111 |
| net_avg_loss | -56.8100 |
| avg_hold_time_bars | 16.0187 |
| exposure | 0.5628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
