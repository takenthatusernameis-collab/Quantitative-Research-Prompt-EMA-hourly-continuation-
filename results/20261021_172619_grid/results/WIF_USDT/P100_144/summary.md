# EMA Hourly Continuation — WIF/USDT P100_144

**Symbol:** WIF/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.5304 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.6620 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -2.6607 |
| sortino_ratio | -0.5218 |
| max_drawdown | 0.4790 |
| cagr | -0.2140 |
| net_avg_win | 65.7277 |
| net_avg_loss | -84.0453 |
| avg_hold_time_bars | 6.0674 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
