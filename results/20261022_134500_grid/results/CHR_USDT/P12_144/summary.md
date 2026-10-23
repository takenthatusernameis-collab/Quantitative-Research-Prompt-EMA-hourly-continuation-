# EMA Hourly Continuation — CHR/USDT P12_144

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7028 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.2757 |
| sortino_ratio | -0.6464 |
| max_drawdown | 0.5504 |
| cagr | -0.2678 |
| net_avg_win | 64.6871 |
| net_avg_loss | -85.5941 |
| avg_hold_time_bars | 39.0969 |
| exposure | 0.7307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
