# EMA Hourly Continuation — AXS/USDT P100_144

**Symbol:** AXS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5384 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0721 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -4.0752 |
| sortino_ratio | -1.2219 |
| max_drawdown | 0.7866 |
| cagr | -0.4552 |
| net_avg_win | 39.7565 |
| net_avg_loss | -74.8171 |
| avg_hold_time_bars | 3.5120 |
| exposure | 0.0726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
