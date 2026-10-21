# EMA Hourly Continuation — YFI/USDT P12_144

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8099 |
| net_win_rate | 0.5249 |
| gross_profit_factor | 1.0889 |
| gross_win_rate | 0.5249 |
| sharpe_ratio | -1.2823 |
| sortino_ratio | -0.3774 |
| max_drawdown | 0.3863 |
| cagr | -0.1605 |
| net_avg_win | 68.7823 |
| net_avg_loss | -93.8408 |
| avg_hold_time_bars | 35.2779 |
| exposure | 0.6721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
