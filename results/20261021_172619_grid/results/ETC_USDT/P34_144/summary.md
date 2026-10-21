# EMA Hourly Continuation — ETC/USDT P34_144

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7118 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.8839 |
| sortino_ratio | -0.5064 |
| max_drawdown | 0.4729 |
| cagr | -0.2067 |
| net_avg_win | 62.6066 |
| net_avg_loss | -85.4932 |
| avg_hold_time_bars | 23.5467 |
| exposure | 0.3778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
