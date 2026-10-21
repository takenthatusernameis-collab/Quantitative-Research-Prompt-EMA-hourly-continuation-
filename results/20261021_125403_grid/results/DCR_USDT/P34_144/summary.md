# EMA Hourly Continuation — DCR/USDT P34_144

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.1126 |
| sortino_ratio | -0.6233 |
| max_drawdown | 0.5444 |
| cagr | -0.2496 |
| net_avg_win | 59.5562 |
| net_avg_loss | -78.3920 |
| avg_hold_time_bars | 17.2116 |
| exposure | 0.3349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
