# EMA Hourly Continuation — DGB/USDT P50_144

**Symbol:** DGB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7049 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.0195 |
| sortino_ratio | -0.5468 |
| max_drawdown | 0.4740 |
| cagr | -0.2223 |
| net_avg_win | 65.3994 |
| net_avg_loss | -83.5011 |
| avg_hold_time_bars | 17.3158 |
| exposure | 0.2841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
