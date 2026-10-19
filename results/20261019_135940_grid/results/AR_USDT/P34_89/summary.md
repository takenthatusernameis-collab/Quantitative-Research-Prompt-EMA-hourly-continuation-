# EMA Hourly Continuation — AR/USDT P34_89

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5347 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8017 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -4.7737 |
| sortino_ratio | -1.7656 |
| max_drawdown | 0.8838 |
| cagr | -0.5755 |
| net_avg_win | 31.6389 |
| net_avg_loss | -50.2460 |
| avg_hold_time_bars | 7.6323 |
| exposure | 0.2425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
