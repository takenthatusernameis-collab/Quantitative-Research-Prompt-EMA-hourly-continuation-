# EMA Hourly Continuation — SHR/USDT P12_100

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.4892 |
| net_win_rate | 0.3569 |
| gross_profit_factor | 0.6617 |
| gross_win_rate | 0.3569 |
| sharpe_ratio | -8.7360 |
| sortino_ratio | -4.0071 |
| max_drawdown | 0.9922 |
| cagr | -0.8532 |
| net_avg_win | 24.4858 |
| net_avg_loss | -27.7847 |
| avg_hold_time_bars | 9.4278 |
| exposure | 0.4637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
