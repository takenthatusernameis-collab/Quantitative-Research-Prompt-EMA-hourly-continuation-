# EMA Hourly Continuation — BAT/USDT P26_200

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6337 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.5446 |
| sortino_ratio | -0.6986 |
| max_drawdown | 0.6103 |
| cagr | -0.2820 |
| net_avg_win | 53.1081 |
| net_avg_loss | -78.6755 |
| avg_hold_time_bars | 33.6816 |
| exposure | 0.5818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
