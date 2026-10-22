# EMA Hourly Continuation — TWT/USDT P21_89

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.5208 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -5.6853 |
| sortino_ratio | -2.2748 |
| max_drawdown | 0.9443 |
| cagr | -0.6717 |
| net_avg_win | 27.2126 |
| net_avg_loss | -44.9423 |
| avg_hold_time_bars | 9.9346 |
| exposure | 0.3662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
