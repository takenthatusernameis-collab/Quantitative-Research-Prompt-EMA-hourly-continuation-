# EMA Hourly Continuation — SKY/USDT P12_89

**Symbol:** SKY/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6676 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9821 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -3.6898 |
| sortino_ratio | -1.3501 |
| max_drawdown | 0.7718 |
| cagr | -0.4733 |
| net_avg_win | 55.3863 |
| net_avg_loss | -78.2403 |
| avg_hold_time_bars | 18.0018 |
| exposure | 0.5481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
