# EMA Hourly Continuation — ETN/USDT P34_144

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.4856 |
| net_win_rate | 0.4047 |
| gross_profit_factor | 0.7224 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -6.3824 |
| sortino_ratio | -2.2948 |
| max_drawdown | 0.9073 |
| cagr | -0.6731 |
| net_avg_win | 38.2860 |
| net_avg_loss | -53.6085 |
| avg_hold_time_bars | 11.0871 |
| exposure | 0.3318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
