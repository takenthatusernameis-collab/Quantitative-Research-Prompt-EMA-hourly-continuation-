# EMA Hourly Continuation — FLR/USDT P34_144

**Symbol:** FLR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6875 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.8933 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.4375 |
| sortino_ratio | -0.7396 |
| max_drawdown | 0.5738 |
| cagr | -0.2879 |
| net_avg_win | 58.7229 |
| net_avg_loss | -77.1565 |
| avg_hold_time_bars | 15.3179 |
| exposure | 0.3154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
