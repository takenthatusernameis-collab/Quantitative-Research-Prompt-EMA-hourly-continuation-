# EMA Hourly Continuation — 1INCH/USDT P12_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8375 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -3.0881 |
| sortino_ratio | -0.7944 |
| max_drawdown | 0.6470 |
| cagr | -0.3205 |
| net_avg_win | 58.5009 |
| net_avg_loss | -80.0200 |
| avg_hold_time_bars | 50.5752 |
| exposure | 0.7793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
