# EMA Hourly Continuation — BAT/USDT P8_144

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6906 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -2.4953 |
| sortino_ratio | -0.7919 |
| max_drawdown | 0.6336 |
| cagr | -0.3078 |
| net_avg_win | 54.9436 |
| net_avg_loss | -77.0396 |
| avg_hold_time_bars | 32.8012 |
| exposure | 0.7425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
