# EMA Hourly Continuation — BCH/USDT P12_89

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.5527 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -6.0280 |
| sortino_ratio | -2.3147 |
| max_drawdown | 0.9415 |
| cagr | -0.6770 |
| net_avg_win | 34.7321 |
| net_avg_loss | -51.2160 |
| avg_hold_time_bars | 14.5295 |
| exposure | 0.4927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
