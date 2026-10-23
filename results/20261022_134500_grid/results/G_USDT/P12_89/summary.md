# EMA Hourly Continuation — G/USDT P12_89

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5439 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8071 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -4.1889 |
| sortino_ratio | -1.4531 |
| max_drawdown | 0.7982 |
| cagr | -0.5013 |
| net_avg_win | 39.3814 |
| net_avg_loss | -58.7155 |
| avg_hold_time_bars | 21.5769 |
| exposure | 0.5979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
