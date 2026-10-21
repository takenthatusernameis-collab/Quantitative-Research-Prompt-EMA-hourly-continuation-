# EMA Hourly Continuation — DIA/USDT P89_144

**Symbol:** DIA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7000 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.1220 |
| sortino_ratio | -0.5445 |
| max_drawdown | 0.4859 |
| cagr | -0.2203 |
| net_avg_win | 69.7277 |
| net_avg_loss | -93.0489 |
| avg_hold_time_bars | 8.1796 |
| exposure | 0.1196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
