# EMA Hourly Continuation — YFI/USDT P12_89

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.5259 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9772 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -5.6240 |
| sortino_ratio | -2.1706 |
| max_drawdown | 0.9334 |
| cagr | -0.6514 |
| net_avg_win | 29.3093 |
| net_avg_loss | -48.5547 |
| avg_hold_time_bars | 16.0979 |
| exposure | 0.5507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
