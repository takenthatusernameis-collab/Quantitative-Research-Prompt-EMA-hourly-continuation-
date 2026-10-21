# EMA Hourly Continuation — GTC/USDT P12_55

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7192 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.7720 |
| sortino_ratio | -1.0064 |
| max_drawdown | 0.7028 |
| cagr | -0.3700 |
| net_avg_win | 56.5398 |
| net_avg_loss | -72.3363 |
| avg_hold_time_bars | 11.9908 |
| exposure | 0.3537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
