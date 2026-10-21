# EMA Hourly Continuation — XMR/USDT P8_55

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7189 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.5894 |
| sortino_ratio | -0.9223 |
| max_drawdown | 0.6576 |
| cagr | -0.3448 |
| net_avg_win | 55.4051 |
| net_avg_loss | -72.9606 |
| avg_hold_time_bars | 12.9420 |
| exposure | 0.3653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
