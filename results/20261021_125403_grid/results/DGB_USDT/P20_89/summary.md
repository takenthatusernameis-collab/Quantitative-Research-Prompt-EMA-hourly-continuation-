# EMA Hourly Continuation — DGB/USDT P20_89

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.7716 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.8943 |
| sortino_ratio | -0.6127 |
| max_drawdown | 0.5180 |
| cagr | -0.2460 |
| net_avg_win | 68.0798 |
| net_avg_loss | -85.5205 |
| avg_hold_time_bars | 14.7793 |
| exposure | 0.3440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
