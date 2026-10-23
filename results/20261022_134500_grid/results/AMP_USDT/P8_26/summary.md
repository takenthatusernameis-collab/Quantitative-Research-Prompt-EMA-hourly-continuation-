# EMA Hourly Continuation — AMP/USDT P8_26

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1940 |
| net_profit_factor | 0.2756 |
| net_win_rate | 0.3675 |
| gross_profit_factor | 0.6652 |
| gross_win_rate | 0.3985 |
| sharpe_ratio | -16.3216 |
| sortino_ratio | -10.1780 |
| max_drawdown | 1.0000 |
| cagr | -0.9947 |
| net_avg_win | 5.3372 |
| net_avg_loss | -11.2514 |
| avg_hold_time_bars | 3.2711 |
| exposure | 0.2885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
