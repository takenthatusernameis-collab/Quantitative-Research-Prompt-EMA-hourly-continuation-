# EMA Hourly Continuation — ID/USDT P12_89

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.7782 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.8450 |
| sortino_ratio | -0.6007 |
| max_drawdown | 0.5368 |
| cagr | -0.2428 |
| net_avg_win | 68.5490 |
| net_avg_loss | -86.0866 |
| avg_hold_time_bars | 22.4828 |
| exposure | 0.5311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
