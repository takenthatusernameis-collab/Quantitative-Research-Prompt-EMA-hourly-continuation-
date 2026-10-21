# EMA Hourly Continuation — ARB/USDT P26_144

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8531 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0389 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -0.9137 |
| sortino_ratio | -0.2421 |
| max_drawdown | 0.3036 |
| cagr | -0.1076 |
| net_avg_win | 82.9535 |
| net_avg_loss | -101.3181 |
| avg_hold_time_bars | 30.5484 |
| exposure | 0.4735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
