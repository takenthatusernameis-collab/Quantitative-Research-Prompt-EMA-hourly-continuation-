# EMA Hourly Continuation — ETH/USDT P34_55

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0317 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -2.2380 |
| sortino_ratio | -0.5237 |
| max_drawdown | 0.4567 |
| cagr | -0.2134 |
| net_avg_win | 54.6447 |
| net_avg_loss | -93.4257 |
| avg_hold_time_bars | 6.6136 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
