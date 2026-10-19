# EMA Hourly Continuation — JST/USDT P89_144

**Symbol:** JST/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.3159 |
| net_win_rate | 0.4126 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -6.9484 |
| sortino_ratio | -2.1133 |
| max_drawdown | 0.9333 |
| cagr | -0.6557 |
| net_avg_win | 23.3925 |
| net_avg_loss | -52.0054 |
| avg_hold_time_bars | 6.6368 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
