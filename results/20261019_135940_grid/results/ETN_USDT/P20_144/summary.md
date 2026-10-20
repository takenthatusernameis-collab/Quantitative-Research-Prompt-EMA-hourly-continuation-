# EMA Hourly Continuation — ETN/USDT P20_144

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.4239 |
| net_win_rate | 0.3669 |
| gross_profit_factor | 0.6190 |
| gross_win_rate | 0.3771 |
| sharpe_ratio | -7.8245 |
| sortino_ratio | -2.8929 |
| max_drawdown | 0.9531 |
| cagr | -0.7619 |
| net_avg_win | 32.5396 |
| net_avg_loss | -44.4902 |
| avg_hold_time_bars | 14.3840 |
| exposure | 0.4578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
