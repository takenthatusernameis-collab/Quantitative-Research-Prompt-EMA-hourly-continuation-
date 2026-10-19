# EMA Hourly Continuation — TAO/USDT P89_144

**Symbol:** TAO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -4.9010 |
| sortino_ratio | -1.4780 |
| max_drawdown | 0.8440 |
| cagr | -0.5211 |
| net_avg_win | 50.7576 |
| net_avg_loss | -73.1877 |
| avg_hold_time_bars | 4.2931 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
