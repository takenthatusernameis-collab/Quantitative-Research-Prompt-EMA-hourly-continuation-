# EMA Hourly Continuation — YGG/USDT P12_89

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.8157 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.6243 |
| sortino_ratio | -0.5372 |
| max_drawdown | 0.5013 |
| cagr | -0.2206 |
| net_avg_win | 77.6265 |
| net_avg_loss | -93.0718 |
| avg_hold_time_bars | 21.3810 |
| exposure | 0.5205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
