# EMA Hourly Continuation — ALT/USDT P12_34

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.5673 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -6.6435 |
| sortino_ratio | -3.0908 |
| max_drawdown | 0.9774 |
| cagr | -0.7768 |
| net_avg_win | 25.5151 |
| net_avg_loss | -37.9449 |
| avg_hold_time_bars | 5.2160 |
| exposure | 0.2601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
