# EMA Hourly Continuation — RPL/USDT P89_200

**Symbol:** RPL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7443 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.6645 |
| sortino_ratio | -0.4116 |
| max_drawdown | 0.3913 |
| cagr | -0.1732 |
| net_avg_win | 76.0009 |
| net_avg_loss | -95.5605 |
| avg_hold_time_bars | 15.6159 |
| exposure | 0.2134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
