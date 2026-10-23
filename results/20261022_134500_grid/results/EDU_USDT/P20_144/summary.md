# EMA Hourly Continuation — EDU/USDT P20_144

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6796 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9055 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.5934 |
| sortino_ratio | -0.8335 |
| max_drawdown | 0.6516 |
| cagr | -0.3276 |
| net_avg_win | 53.6768 |
| net_avg_loss | -72.0597 |
| avg_hold_time_bars | 24.1698 |
| exposure | 0.5731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
