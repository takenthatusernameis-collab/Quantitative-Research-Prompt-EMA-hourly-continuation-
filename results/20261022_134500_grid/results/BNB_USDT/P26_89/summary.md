# EMA Hourly Continuation — BNB/USDT P26_89

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.3407 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -8.4448 |
| sortino_ratio | -3.2334 |
| max_drawdown | 0.9864 |
| cagr | -0.8168 |
| net_avg_win | 16.0179 |
| net_avg_loss | -35.5171 |
| avg_hold_time_bars | 9.0230 |
| exposure | 0.3031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
