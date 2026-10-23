# EMA Hourly Continuation — SLP/USDT P26_89

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.6353 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -5.0486 |
| sortino_ratio | -2.0166 |
| max_drawdown | 0.9162 |
| cagr | -0.6207 |
| net_avg_win | 42.3826 |
| net_avg_loss | -58.7255 |
| avg_hold_time_bars | 8.7391 |
| exposure | 0.3182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
