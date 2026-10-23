# EMA Hourly Continuation — CHR/USDT P26_89

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5957 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -4.5728 |
| sortino_ratio | -1.7212 |
| max_drawdown | 0.8783 |
| cagr | -0.5603 |
| net_avg_win | 39.0278 |
| net_avg_loss | -55.7237 |
| avg_hold_time_bars | 10.0279 |
| exposure | 0.3258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
