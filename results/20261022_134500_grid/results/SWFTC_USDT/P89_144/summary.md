# EMA Hourly Continuation — SWFTC/USDT P89_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.4145 |
| net_win_rate | 0.3866 |
| gross_profit_factor | 0.7303 |
| gross_win_rate | 0.4011 |
| sharpe_ratio | -7.0542 |
| sortino_ratio | -2.3513 |
| max_drawdown | 0.9472 |
| cagr | -0.6890 |
| net_avg_win | 31.4692 |
| net_avg_loss | -47.8421 |
| avg_hold_time_bars | 4.7677 |
| exposure | 0.1194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
